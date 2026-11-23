FROM public.ecr.aws/d3j8x8q7/olympus-base-typescript:latest
WORKDIR /app
# Use the provided pnpm with the frozen lock; no runtime tool downloads.
ENV npm_config_manage_package_manager_versions=false
COPY . .
# The pinned repository includes pnpm-lock.yaml; COPY above includes it.
# Source tests need no dist build or optional sharp/zstd/liblzma build hooks.
# Locked platform-specific optional packages supply the bundler binaries.
RUN pnpm install --frozen-lockfile --ignore-scripts --prod=false
CMD ["/bin/bash"]
