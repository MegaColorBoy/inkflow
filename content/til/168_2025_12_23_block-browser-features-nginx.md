title: Block browser features with permissions policy in Nginx
date: December 23rd, 2025
slug: block-browser-features-with-permissions-policy-in-nginx
category: nginx + Security
status: active

Recently, I learned that you can explicitly disable browser features like **camera, microphone, and geolocation** using the `Permissions-Policy` HTTP response header.

Using a single line in nginx, it does the job:

```nginx
add_header Permissions-Policy "camera=(), microphone=(), geolocation=()" always;
```

## What this does?

* Disables camera access
* Disables microphone access
* Disables geolocation access
* Applies to all origins
* The browser won’t even prompt the user for permission

The empty `()` means **no origins are allowed** to use these features.

## Why this is useful?

* Improves security and privacy
* Prevents misuse by third-party scripts
* Good default for content sites, admin panels, and APIs

The `always` flag ensures the header is sent even on error responses (404, 500, etc.).

Hope you found this tip useful!