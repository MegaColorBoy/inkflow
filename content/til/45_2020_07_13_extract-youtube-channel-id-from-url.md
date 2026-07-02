title: Extract YouTube Channel ID from URL
date: July 13th, 2020
slug: extract-youtube-channel-id-from-url
category: PHP
status: active

Using PHP's in-built function, `parse_url`, you can write a helper method to pull the channel ID off a YouTube URL especially if you're pulling videos using YouTube's Data API. Here's the code:
```php
<?php
public function extractChannelID($url){
    // Parse the link and trim any whitespaces
    $parsed_link = parse_url(rtrim($url, '/'));

    // Return the channel ID if it matches the pattern
    if (isset($parsed_link['path']) && preg_match('/^\/channel\/(([^\/])+?)$/', $parsed_link['path'], $matches)) {
        return $matches[1];
    }

    throw new Exception("This {$url} is not a valid YouTube channel URL");
    return null;
}
?>
```

Writing tiny methods like these can help save time and be reusable in more than one context. 

Hope you find this tip useful! &#x1F601;