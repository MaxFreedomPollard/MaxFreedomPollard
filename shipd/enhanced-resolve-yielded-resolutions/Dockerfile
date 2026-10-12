FROM public.ecr.aws/d3j8x8q7/olympus-base-typescript:latest
WORKDIR /app
# npm ci installs exactly the versions in the committed package-lock.json and
# refuses to run without one; copying the lockfile explicitly makes the build
# fail if it is ever missing, so the install below is fully pinned and
# reproducible. --include=dev is needed because the base image sets
# NODE_ENV=production and the test runner is a dev dependency; --ignore-scripts
# skips the husky prepare hook.
COPY package.json package-lock.json ./
RUN npm ci --include=dev --ignore-scripts
COPY . .
# The repository's own test/simple.test.js resolves the checkout by the name
# "enhanced-resolve" from its parent directory; the symlink gives the checkout
# that name so the project's full suite runs unchanged.
RUN ln -sfn /app /enhanced-resolve
CMD ["/bin/bash"]
