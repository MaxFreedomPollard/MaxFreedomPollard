FROM public.ecr.aws/d3j8x8q7/olympus-base-go:latest
WORKDIR /app
COPY go.* ./
# This pinned module uses only the Go standard library; no go.sum is required.
RUN go mod download
COPY . .
RUN go build ./...
RUN groupadd -g 1000 model && useradd -u 1000 -g model -m model
RUN chown -R model:model /app
USER model
CMD ["/bin/bash"]
