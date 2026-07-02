title: Extract unique characters from a string
date: August 23rd, 2020
slug: extract-unique-characters-from-a-string
category: Python
status: active

I thought of getting back into competitive programming again and 
started practicing my python coding-chops on [Codewars](https://www.codewars.com).

Here's a neat trick on how to extract unique characters from a string:

```python
from collections import OrderedDict

word = "HelloWorld"
uniq = ''.join(OrderedDict.fromkeys(word).keys())

print(uniq) # prints HeloWrd
```

Using `OrderedDict` allows you to preserve the order in which the keys are inserted as a normal `dict` doesn't track the order.

Hope you found this useful!