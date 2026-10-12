Add lazy streaming iteration for yielding resolutions. Fix yielded exports results, duplicate delivery and unsafe-cache transparency.

In asynchronous yielding mode across all resolver routes, every result goes to resolveContext.yield; successful completion returns undefined, and failures report their original error after any delivered prefix. Genuine exports misses still fail without deliveries.

Deliver each distinct path/query/fragment tuple once per resolution. Suppressed duplicates still count as found. Never expose internal restriction bookkeeping.

An ordinary fallback-only answer must not hide a package created before the next call. Keep ordinary and yielding entries separate.

For yielding resolutions, capture the complete described-resolve outcome. Include configured fallback even after a package yields, and eligible public after-described-resolve taps. Warm replay must deliver the saved results without invoking these sources again. Preserve the callback outcome separately from yielded values: yield-only completion allows parent routes to continue; a returned terminal request still stops them. Publish new yielding entries only after the whole resolution succeeds, not when an inner route completes. Failures retain their uncached prefix and leave no newly reusable answers.

Top-level consumer edits must not affect later deliveries or replays.

Provide Resolver.resolveIterator, package-level iterate and the create.iterate(options) factory. Resolution calls accept (parent, request, iteratorContext?) or (context, parent, request, iteratorContext?), preserving the corresponding promise API's context defaults. A file URL in the first argument is a parent, not a context object.

These requirements concern JavaScript runtime behavior; TypeScript declarations, synchronous resolution APIs and cache dependency capture or replay are outside this task. The iterator context accepts native AbortController signals. Every call returns a new self-iterating asynchronous iterator of full request objects, including path:false.

Only the first next starts resolution work; stream values before completion, including on cold cache misses. Match buffered values and outstanding reads FIFO. Success drains the buffer before done/undefined. On any resolver failure, including a synchronous startup throw after deliveries, first drain any buffered prefix. Then reject pending and subsequent reads with the original error.

return(value) discards buffered results and resolves pending reads as done with undefined; later reads are also done. It resolves its own call as done with value. throw(error) discards buffered results and rejects pending reads with that error; later reads are done. It rejects its own call with the same error. Both work before first next, ignore late producer activity and replace earlier errors with done.

Pre-abort prevents resolution. In-flight abort discards buffers and persistently rejects reads with an Error named AbortError, independent of signal.reason. Release signal listeners on success, failure, return, throw and abort. Abort after producer completion has no effect, even with buffered results.
