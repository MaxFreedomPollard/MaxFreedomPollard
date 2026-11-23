FROM public.ecr.aws/d3j8x8q7/olympus-base-go:latest
WORKDIR /app

# test.sh converts the JSON output of go test into JUnit XML with go-junit-report.
# The release is pinned so every build installs the same tool.
RUN GOBIN=/usr/local/bin go install github.com/jstemmer/go-junit-report/v2@v2.1.0

# Install the official native patch helper independently of the solver harness.
RUN set -eu; \
    case "$(uname -m)" in \
        x86_64) patch_target=x86_64-unknown-linux-musl; patch_sha256=306865417d4ee7a927785852910a527f41e1e159add390ac5ae3accb67d44a13 ;; \
        aarch64|arm64) patch_target=aarch64-unknown-linux-musl; patch_sha256=883620139925f677e5a12c95ba87a1d7f421388ebb797b1c10aba42a04ede9d7 ;; \
        *) printf '%s\n' 'Unsupported patch-helper architecture' >&2; exit 1 ;; \
    esac; \
    mkdir -p /opt/codex-patch; \
    curl -fL --retry 3 "https://github.com/openai/codex/releases/download/rust-v0.160.0/codex-${patch_target}.tar.gz" -o /tmp/codex-patch.tar.gz; \
    printf '%s  %s\n' "$patch_sha256" /tmp/codex-patch.tar.gz | sha256sum -c -; \
    tar -xzf /tmp/codex-patch.tar.gz -C /opt/codex-patch "codex-${patch_target}"; \
    test -x "/opt/codex-patch/codex-${patch_target}"; \
    ln -s "/opt/codex-patch/codex-${patch_target}" /usr/local/bin/apply_patch; \
    rm /tmp/codex-patch.tar.gz

COPY . .

# The repository commits its vendor/ directory, and -mod=vendor makes the build use it,
# so nothing is downloaded; if vendor/ were missing, the modules are downloaded here
# at build time and test.sh builds from that module cache with GOPROXY=off.
# The build fills the build cache, and the cache is made writable for any user because
# the tests may run as a non-root user.
RUN if [ -d vendor ]; then FLAGS="-mod=vendor"; else go mod download && FLAGS=""; fi \
    && go build $FLAGS ./pkg/smbios/... ./cmds/exp/dmidecode/... \
    && go vet $FLAGS ./pkg/smbios/... ./cmds/exp/dmidecode/... \
    && chmod -R a+rwX /opt/go/cache

CMD ["/bin/bash"]
