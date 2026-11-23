FROM public.ecr.aws/d3j8x8q7/olympus-base-typescript:latest
WORKDIR /app
COPY . .
# The repository commits package-lock.json, so `npm ci` installs the exact
# locked versions; fail the build loudly if that lockfile ever goes missing.
RUN test -f package-lock.json
RUN npm ci --include=dev --ignore-scripts
# Mock file access is controlled by file mode, and a process running as root
# bypasses those checks, so the suite runs as a normal user.
RUN groupadd -g 1000 model && useradd -u 1000 -g model -m model
RUN chown -R model:model /app
USER model
CMD ["/bin/bash"]
