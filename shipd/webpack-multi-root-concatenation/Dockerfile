FROM public.ecr.aws/d3j8x8q7/olympus-base-typescript:latest

WORKDIR /app

# Override the base image's NODE_ENV=production so yarn install and webpack's
# `yarn setup` / `yarn lint` preserve devDependencies at build time and runtime.
# HUSKY=0 prevents `yarn setup` from rewriting .git/config during offline lint runs.
ENV NODE_ENV=development \
    HUSKY=0

# yarn.lock is committed, so --frozen-lockfile pins every dependency without
# rewriting the lockfile, and --ignore-engines matches .yarnrc without copying
# .yarnrc before dependency installation.
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile --ignore-engines

COPY . .
# Uninitialize optional external test corpora submodules so `tsconfig.types.test.json`
# matches a standard git clone without external benchmark configs, then restore
# webpack's self-link and verify devDependencies are present.
RUN if [ -d .git ]; then git submodule deinit -f --all 2>/dev/null || true; fi \
    && find test/external -mindepth 2 -maxdepth 2 -exec rm -rf {} + \
    && ln -sfn .. node_modules/webpack \
    && test -d node_modules/prettier-2 \
    && test -d node_modules/jest-cli \
    && test -d node_modules/jest-junit

CMD ["/bin/bash"]
