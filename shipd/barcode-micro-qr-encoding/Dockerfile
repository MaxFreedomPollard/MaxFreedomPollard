FROM public.ecr.aws/d3j8x8q7/olympus-base-go:latest
WORKDIR /app

# test.sh converts the JSON output of go test to JUnit XML with go-junit-report.
# The release is pinned so every build installs the same tool.
RUN GOBIN=/usr/local/bin go install github.com/jstemmer/go-junit-report/v2@v2.1.0

COPY . .

# The module has no dependencies. Compiling every package fills the build
# cache; no test runs during the build.
RUN go build ./...

CMD ["/bin/bash"]
