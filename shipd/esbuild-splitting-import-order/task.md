Consider this code bundled with `esbuild --bundle --outdir=build --format=esm --splitting --platform=node --out-extension:.js=.mjs ./entry1.js ./entry2.js` (or `api.Build` with `Bundle: true`, `Splitting: true`, `Format: api.FormatESModule`):

```js
// entry1.js
import "./init-dep-1.js";
import "./run-dep.js";

// entry2.js
import "./init-dep-2.js";
import "./run-dep.js";

// init-dep-1.js
globalThis.foo = { log: () => console.log("entry 1") };

// init-dep-2.js
globalThis.foo = { log: () => console.log("entry 2") };

// run-dep.js
globalThis.foo.log();
```

`esbuild` moves `run-dep.js` into a shared chunk and imports it above `init-dep-1.js` and `init-dep-2.js`, crashing at runtime with `TypeError: Cannot read properties of undefined`.

Please fix code-split ESM bundling so every entry runs its live modules in ECMA-262 `InnerModuleEvaluation` depth-first post-order. That covers entry-local setup, agreeing or conflicting shared chunks, diamonds (shared leaves run once), synchronous cycles, live `export let` bindings, top-level functions and classes, `export { ... } from`, `export * from`, top-level `await`, dynamic `import()` sharing modules with static entries, CommonJS imports, and static `External` imports ordered relative to both bundled modules and other externals.

Keep shared modules in non-entry shared chunks instead of copying them into each entry, and keep existing splitting output when chunks only export pure literals or functions or already match ECMA-262 order. Unused modules and unused `/* @__PURE__ */` calls (including selective `sideEffects: false` barrels) must stay tree-shakeable, while live `/* @__PURE__ */` calls must not get reordered ahead of earlier modules. Default `.js`/`.mjs` extensions, `MinifyWhitespace`/`MinifyIdentifiers`/`MinifySyntax`, linked `Sourcemap` (`.map` files), and deduplicated `Metafile` external `imports` should all keep working.
