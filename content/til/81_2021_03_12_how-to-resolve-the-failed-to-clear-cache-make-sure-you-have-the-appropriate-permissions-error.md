title: How to resolve the "Failed to clear cache. Make sure you have the appropriate permissions." error
date: March 12th, 2021
slug: how-to-resolve-the-failed-to-clear-cache-make-sure-you-have-the-appropriate-permissions-error
category: Laravel
status: active

This error is annoying and mostly happens if the `data` directory is missing under the `storage/framework/cache/data` directory. For some reason, this folder doesn't exist by default.

To resolve it, just manually create the `data` directory under the `storage/framework/cache/data` directory and it should fix the issue.