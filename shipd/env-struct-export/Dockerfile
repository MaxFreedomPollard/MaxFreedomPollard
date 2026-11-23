FROM public.ecr.aws/d3j8x8q7/olympus-base-go:latest
WORKDIR /app
ENV GOTOOLCHAIN=local
ENV GOFLAGS=-mod=readonly
COPY go.mod go.sum ./
RUN go mod download && go mod verify
COPY . .
RUN go build -p 2 ./...
CMD ["/bin/bash"]
