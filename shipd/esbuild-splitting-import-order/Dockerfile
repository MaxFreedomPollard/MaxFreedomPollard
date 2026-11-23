FROM public.ecr.aws/d3j8x8q7/olympus-base-go:latest
WORKDIR /app
ENV GOTOOLCHAIN=local

# Verify preinstalled Node.js (used for end-to-end ESM bundle execution tests)
# and ensure go-junit-report is available if not already preinstalled.
RUN node --version \
    && (command -v go-junit-report >/dev/null 2>&1 || GOBIN=/usr/local/bin go install github.com/jstemmer/go-junit-report/v2@v2.1.0)

COPY go.mod go.sum ./
RUN go mod download && go mod verify

COPY . .

# Pre-build packages from clean source without running tests, and make the Go
# module and build caches readable/writable for non-root offline test runs.
RUN go build ./... \
    && chmod -R a+rwX "$(go env GOCACHE)" "$(go env GOMODCACHE)"

CMD ["/bin/bash"]
