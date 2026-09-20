title: Test API CORS headers using curl
date: September 19th, 2026
slug: test-api-cors-headers-using-curl
category: HTTP + curl + DevOps
status: active

When troubleshooting an API request from a browser, I find it useful to inspect the CORS headers directly with curl. It makes it easier to see what the server is returning.

For a cross-origin JSON POST request with an authorization header, start by simulating the browser's preflight request:

```bash
curl -i -X OPTIONS 'https://api.example.com/endpoint' \
  -H 'Origin: https://example.com' \
  -H 'Access-Control-Request-Method: POST' \
  -H 'Access-Control-Request-Headers: content-type, authorization'
```

Replace both URLs with your API endpoint and frontend origin. An illustrative successful response could look like this:

```http
HTTP/1.1 204 No Content
Access-Control-Allow-Origin: https://example.com
Access-Control-Allow-Methods: POST, OPTIONS
Access-Control-Allow-Headers: content-type, authorization
Vary: Origin
```

Next, test the actual POST request:

```bash
curl -i 'https://api.example.com/endpoint' \
  -H 'Origin: https://example.com' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  --data '{"message":"Testing CORS"}'
```

Use a suitable test endpoint and payload: this sends a real POST request. Replace the token if authentication is required, or remove that header if it isn't.

Notice that the `Access-Control-Request-*` headers belong to the preflight. The actual POST carries the content type and authorization header themselves.

An example POST response might be:

```http
HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: https://example.com
Vary: Origin

{"message":"Request received"}
```

Check the CORS headers on both responses. A successful preflight alone isn't enough if the actual response is missing the required headers.

For browser requests made with credentials, such as cookies using `credentials: 'include'`, the server must allow the specific origin and return `Access-Control-Allow-Credentials: true`; a wildcard origin won't work for those requests.

Finally, curl displays the response but doesn't enforce CORS like a browser does. Confirm the behavior in your browser too. The [MDN CORS guide](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) explains how the browser evaluates these responses.

Hope you found this tip useful!
