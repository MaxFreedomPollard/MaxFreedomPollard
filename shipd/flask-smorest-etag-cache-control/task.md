ETag is a web cache validation mechanism. It allows an API client to make conditional requests. The ETag feature is available through the `Blueprint.etag` decorator (`enabled`, `weak`, `include_headers`), `Blueprint.cache_control`, and `Blueprint` (`etag`, `etag_weak`, `etag_include_headers`, `cache_control`), applying outer-to-inner across nested blueprints, `MethodView`, and view functions for any decorator or `register_blueprint` order:
  check_etag (optional weak=False) -> strong If-Match check
  set_etag and auto-ETag -> resolve weak (explicit>endpoint>blueprint>False) and case-insensitive include_headers in response.headers order, with weak If-None-Match checks

`Cache-Control` directives (strings, mappings, iterables, or kwargs) with stripped lowercase `"_"`->`"-"` names merge in place across layers (or clear on `False`):
  formatting -> True/"" formats as name, int>=0 as name=val (ValueError if <0), and str as name="val" (if whitespace/comma) or name=val
  updating -> False/None removes keys, and public/private are mutually exclusive

When ETag is computed with response data, that data may contain headers. It can be disabled globally with the `ETAG_DISABLED` application parameter across sync/async views and OpenAPI specs:
  200<=status_code<400 -> sets non-empty Cache-Control on the response when absent before automatic ETag computation
  304 NotModified(headers=None) -> includes ETag plus active Cache-Control
