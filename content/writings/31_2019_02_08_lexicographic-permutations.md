title: Lexicographic Permutations
date: May 25th, 2018
slug: lexicographic-permutations
category: Algorithms + Data Structures
summary: How to generate the next permutation of any given sequence in lexicographical order.

According to [Problem 24](https://projecteuler.net/problem=24) in Project Euler, you are asked to find the millionth permutation using the following sequence of 10 digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9). Well, if you do the math, there are around ***10! = 3,628,800 unique permutations*** and that means, you have to come up with an efficient algorithm.

I tried writing a recursive function but it turned out to be a bit tricky, so I thought of writing a brute-force solution which seemed far more simpler to understand and it's quite efficient.

## Algorithm Description

The following algorithm is quite simple and easy to understand:

```text
1. Find i such that a[i-1] is greater than or equal to a[i].
2. Find j such that a[j-1] is less than or equal to a[i-1].
3. Swap a[i] with a[j].
4. Reverse the suffix from a[i+1] to the last element.
```

Suppose, if the first step fails, it means the current permutation is the last one because such an index that does not exist. However, it's simple to implement the following algorithm correctly and efficiently, so let's take a look at the implementation.

## Python Implementation

The following method only generates the next permutation of any given sequence, so if you're interested in generating all the permutations, especially, for very large lists, this function can be useful.

**Implementation of the method(s):**

```python
# Swap numbers in a list
def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

# Get the next permutation
def nextPermutation(list):
    
    i = len(list) - 1

    # As long as the f(x-1) >= f(x), decrement the first index
    while list[i-1] >= list[i]:
        i = i-1

    j = len(list)

    # As long as the f(y-1) <= f(x-1), decrement the second index
    while list[j-1] <= list[i-1]:
        j = j-1

    # make a swap
    swap(list, i-1, j-1)

    i = i+1
    j = len(list)

    # keep swapping until you get the next permutation
    while i < j:
        swap(list, i-1, j-1)
        i = i+1
        j = j-1

    return list
```

**Final code:**

```python
#!usr/bin/python
import math, time, pe_lib

start = time.time()

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 1
limit = 1000000

while count < limit:
    pe_lib.nextPermutation(list)
    count = count + 1

print "".join(str(x) for x in list)
print "Finished: %f seconds" % (time.time() - start)
```

This code in executed in approximately **2.37 seconds** with an algorithmic complexity of **O(n)** i.e. linear time complexity and the replacements of the numbers were done [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) since no extra space was used.

Hope you liked reading this article!

## References

+ [Counting and Listing all Permutations](https://www.cut-the-knot.org/do_you_know/AllPerm.shtml)
+ [LeetCode: Next Permutation](https://leetcode.com/articles/next-permutation)