title: How to resolve the "file_get_contents(): SSL operation failed" error
date: March 12th, 2021
slug: how-to-resolve-the-filegetcontents-ssl-operation-failed-error
category: PHP
status: active

If you're facing this error while trying to download a file from your server, it's most probably the SSL certificate that has been hosted on your server isn't correctly verified or maybe, you're using OpenSSL on a server running PHP 5.6.

As per the [documentation](http://php.net/manual/en/migration56.openssl.php), there are some changes that can be made to resolve it, like the following method:

```php
<?php
public function foo(Request $request) {
    $arrContextOptions = array(
        "ssl" =&gt; array(
            "verify_peer" =&gt; false,
            "verify_peer_name" =&gt; false,
        ),
    );
    return Response::make(file_get_contents(asset('pdf/file.pdf'), false, stream_context_create($arrContextOptions)), 200, [
        'Content-Type' =&gt; 'application/pdf',
        'Content-Disposition' =&gt; 'inline; filename="file.pdf"',
    ]);
}
?>
```

Although, I won't recommend this unless you are testing it on a `localhost` environment as it's not secure and could have significant security implications because disabling verification can permit a [Man in the Middle attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) to take place.

Use it at your own risk!