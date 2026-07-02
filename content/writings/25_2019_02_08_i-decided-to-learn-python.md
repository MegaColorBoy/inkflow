title: I decided to learn Python
date: February 3rd, 2018
slug: i-decided-to-learn-python
category: Algorithms + Programming
summary: I decided to get back on solving algorithmic and programming puzzles by adding a new programming language to my tech arsenal, Python.

Hello Folks!

Happy New Year! I know I'm late at this point but hey, it's better late
than never!

As the year had begun, I got busy with work and I barely found any time
to post anything new but that doesn't mean I didn't do anything new.

At the end of December, I decided to get back on solving algorithmic and
programming puzzles again (The last time I did was back on 2016) and for
starters, I decided to solve [Project Euler](http://projecteuler.net)
problems by adding a new programming language to my tech arsenal,
***Python***.

## Why solve it using Python?

Previously, I'd solved around 57 problems using ***C++*** and it got
paused for a while after I got into internships and work life. But now
that I have found the time for it, I thought that this would be the
perfect opportunity for me to learn Python. It has a really good
community, good documentation and the code looks so clean, simple and
readable without those curly brackets!

## What is Project Euler?

It's a website that hosts a series of challenging algorithmic and
mathematical programming puzzles in which you will have to produce
solutions that'd ***clock in under a minute*** with decent computer
specifications.

By solving these puzzles, you will be experiencing an ***inductive chain
learning*** i.e. when you solve one problem, you'll be exposed to a
completely new concept that allows you to delve into unfamiliar areas of
mathematics and programming.

As I'm writing this article, I'm taking it slow and I have solved around
21 problems in 3 weekends. I will be posting a walkthrough for each
problem but for now, I will talk about one of my favorite problems:
***Maximum Path Sum***.

## Maximum Path Sum

Problem definition of [Problem 18](https://projecteuler.net/problem=18):

By starting at the top of the Binary Tree below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

<p style="text-align:center;font-family:'FiraMono';font-size:12pt;"><span style="color:#ff0000;"><b>3</b></span><br><span style="color:#ff0000;"><b>7</b></span> 4<br>
2 <span style="color:#ff0000;"><b>4</b></span> 6<br>
8 5 <span style="color:#ff0000;"><b>9</b></span> 3</p>

That is, 3 + 7 + 4 + 9 = 23. Now, find the maximum total from top to bottom of the Binary Tree below:

<p style="text-align:center;font-family:'FiraMono';">
75<br>
95 64<br>
17 47 82<br>
18 35 87 10<br>
20 04 82 47 65<br>
19 01 23 75 03 34<br>
88 02 77 73 07 63 67<br>
99 65 04 28 06 16 70 92<br>
41 41 26 56 83 40 80 70 33<br>
41 48 72 33 47 32 37 16 94 29<br>
53 71 44 65 25 43 91 52 97 51 14<br>
70 11 33 28 77 73 17 78 39 68 17 57<br>
91 71 52 38 17 14 91 43 58 50 27 29 48<br>
63 66 04 68 89 53 67 30 73 16 69 87 40 31<br>
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
</p>

Since there are fifteen rows, you can solve this puzzle using Brute
Force by trying every route possible but if you're going to use that
same technique for [Problem 67](https://projecteuler.net/problem=67)
that has a Binary Tree containing one hundred rows, it will not be
efficient. So this problem forces you to avoid brute force and instead
wants you to come up with a clever solution!

## Solution

As I had mentioned above, a brute force technique is going to be very
inefficient, instead I did a bottom-up approach:

**Implementation of the method(s):**

```python
# Sum of numbers
def sumOfNumbers(n):
    return (n*(n+1))/2

# Return the maximum path sum in a Binary Tree
# Bottom Up Approach
def maxPathSum(list):
    # the last number of the list
    last = len(list)

    # number of rows in the Binary Tree
    nrow = 1

    # count the number of rows in the Binary Tree
    # use the sum of numbers method to count the number of rows
    while sumOfNumbers(nrow) < last:
        # print (sumOfNumbers(nrow))
        nrow += 1

    last -= 1

    for i in range(nrow, 0, -1):
        # print list[last - i]

        # iterate through each number in each row
        for j in range(2, i+1):
            # pick a number from the row above the current row
            # and pick the 2 numbers from the current row
            # Find the max between the two numbers and add it
            list[last - i] = list[last - i] + max(list[last - 1], list[last])
            
            # shift to the next number in the row above
            last -= 1

        # shift to the next number in the row above
        last -= 1

    # return the max sum
    return list[0]
```

**Final code:**

```python
# Project Euler: Problem 18 and 67 - Maximum Path Sum I and II

#!usr/bin/python
import time, math, pe_lib

num_str = ""

# read text file
f = open("triangle2.txt", "r")
for line in f:
    num_str += line
f.close()

# convert the string numbers to integers in the list
list = map(int, num_str.replace('n', ' ').split(' '))

start = time.time()
print pe_lib.maxPathSum(list)
print "Finished: %f seconds" % (time.time() - start)
```

The maximum path sum for ***Problem 67*** is ***7273*** and it compiled in
***0.003990*** seconds.

***Note: This solution and the library named <mark>pe_lib.py</mark> was
built using the Python programming language. The source code for this
solution can be found on Github.***

Stay tuned for more!