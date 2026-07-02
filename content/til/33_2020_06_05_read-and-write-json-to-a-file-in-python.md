title: Read and Write JSON to a file in Python
date: June 5th, 2020
slug: read-and-write-json-to-a-file-in-python
category: Python
status: active

You can make use of the built-in `json` package in Python to read and write JSON data to a file.

## Writing JSON to a file
You can store the information in a dictionary or `dict` object, which can contain any type of data like integers, booleans, arrays or nested objects.

By using a `dict` object, the `json` package will transform your dictionary into a serialized JSON string.
```python
import json

dataObj = {}
dataObj['posts'] = []
dataObj['posts'].append({
    'title': 'Hello world',
    'category': 'Introduction',
    'slug': 'hello-world'
})

with open('data.json', 'w') as file:
    json.dump(dataObj, file)
```

## Reading JSON from a file
Reading is as easy as writing to a file. Using the same package again, we can parse the JSON string directly from the file.
```python
import json

with open('data.json', 'r') as file:
    data = json.load(file)
    for item in data['posts']:
        print 'Title: ' + item['title']
        print 'Category: ' + item['category']
        print 'Slug: ' + item['slug']
```
I read about different package alternatives like `simplejson` but I guess for now, this is a great way to get started especially, if you're working with web applications and are interacting with a serialized JSON data on a daily basis.
