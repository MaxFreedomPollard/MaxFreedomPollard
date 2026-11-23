FROM public.ecr.aws/d3j8x8q7/olympus-base-typescript:latest

WORKDIR /app
COPY package.json package-lock.json ./

# --ignore-scripts is intentional: solution patches modify nunjucks/ after
# image creation, and the verifier loads that source directly. Root prepare
# generates duplicate source trees that would become stale after patching.
# No dependency build is needed for the Node verifier. Assert the complete
# lockfile hook list below: PhantomJS is only used by the browser test runner;
# both fsevents packages are optional and macOS-only. All other dependencies
# ship usable JavaScript. Fail the build if any additional install hook appears.
RUN node -e "const assert = require('assert'); const packages = require('./package-lock.json').packages; const hooks = Object.keys(packages).filter(p => packages[p].hasInstallScript).sort(); assert.deepStrictEqual(hooks, ['node_modules/chokidar/node_modules/fsevents', 'node_modules/fsevents', 'node_modules/phantomjs-prebuilt']);"
RUN npm ci --include=dev --ignore-scripts --no-audit --no-fund

COPY . .
# Resolve module paths without executing repository initialization code.
RUN node -e "['./nunjucks', 'mocha', 'expect.js', 'uglify-js'].forEach(name => require.resolve(name))"

CMD ["/bin/bash"]
