title: LRU Cache - Coderbyte
date: January 2nd, 2022
slug: lru-cache--coderbyte
category: Algorithms
summary: Thought of solving this cache challenge on CoderByte.
status: inactive

Yesterday, I had an online technical assessment sent by a company to see if I'm fit for the role. The question wasn't hard
but it was a bit tricky that I had to see what was the problem really trying to explain.

## What's a cache?
It's quite essential to storing data locally in order to avoid unnecessary calls to the server, API or database.

# What's LRU Cache?
Honestly, I didn't know what is it until I saw this interview question.

```javascript
	function LRUCache(arr) {
		let cache = [];

		for (let char of arr) {
			if(cache.includes(char)) {
				cache.splice(cache.indexOf(char), 1);
			} else if (cache.length >= 5) {
				cache.shift();
			}

			cache.push(char);
		}

		return cache.join('-');
	}
	```
