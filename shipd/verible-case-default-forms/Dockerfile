FROM public.ecr.aws/d3j8x8q7/olympus-base-cpp:latest
WORKDIR /app

# Use the repository's Bazel release and verify its published binary checksum
# before execution. Both supported Linux architectures use the same version.
RUN set -eux; \
    case "$(uname -m)" in \
      x86_64) arch=x86_64; sha=ac6249d1192aea9feaf49dfee2ab50c38cee2454b00cf29bbec985a11795c025 ;; \
      aarch64) arch=arm64; sha=2d86d36db0c9af15747ff02a80e6db11a45d68f868ea8f62f489505c474f0099 ;; \
      *) echo "unsupported architecture"; exit 1 ;; \
    esac; \
    curl -fsSL "https://releases.bazel.build/7.6.1/release/bazel-7.6.1-linux-$arch" -o /usr/local/bin/bazel; \
    echo "$sha  /usr/local/bin/bazel" | sha256sum -c -; \
    chmod 0755 /usr/local/bin/bazel

# The dependency cache is shared across build and runtime users. Local actions
# avoid requiring Linux user namespaces inside the container.
RUN printf 'build --repository_cache=/opt/bazel-repository-cache\nbuild --spawn_strategy=local\ntest --spawn_strategy=local\n' > /etc/bazel.bazelrc

COPY . .

# MODULE.bazel pins external dependencies. Build the affected trees and linter
# now so their source archives are cached before offline use; execute no tests.
RUN bazel build --jobs=8 \
      //verible/verilog/analysis/... \
      //verible/verilog/CST/... \
      //verible/verilog/parser/... \
      //verible/verilog/tools/lint:verible-verilog-lint \
 && bazel shutdown \
 && chmod -R a+rwX /opt/bazel-repository-cache

CMD ["/bin/bash"]
