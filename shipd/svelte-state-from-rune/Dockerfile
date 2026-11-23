FROM public.ecr.aws/d3j8x8q7/olympus-base-typescript:latest

WORKDIR /app

COPY . .

# Pre-install dependencies at build time so tests run offline.
RUN pnpm install --frozen-lockfile

CMD ["/bin/bash"]
