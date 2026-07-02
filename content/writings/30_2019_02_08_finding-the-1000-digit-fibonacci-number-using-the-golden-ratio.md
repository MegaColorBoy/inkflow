title: Finding the 1000 digit Fibonacci number using the Golden Ratio
date: May 18th, 2018
slug: finding-the-1000-digit-fibonacci-number-using-the-golden-ratio
category: Mathematics
summary: Rather than sticking to using a brute force solution, I decided to find the 1000 digit fibonacci number using the Golden Ratio.

Back in February, I said that I'm going to start [solving Project Euler
problems using Python](/posts/i-decided-to-learn-python) and yes, I
have been doing it actively but sometimes, I don't find the time to post
the solutions.

If you're someone who has tried Project Euler before, you'll know that
you'll get to encounter problems that require you to implement smart
solutions to crunch big numbers efficiently. One of those problems is
[Problem 25](https://www.projecteuler.net/problem=25), which states to
find the first term in the [Fibonacci
Sequence](https://en.wikipedia.org/wiki/Fibonacci_number) that contains
1000 digits.

This problem can be easily solved using a Brute Force solution, instead,
I opted to try out a mathematical solution that makes use of the [Golden
Ratio](https://en.wikipedia.org/wiki/Golden_ratio) and also, it gave me
the perfect excuse to try writing those formulas using
[LaTeX](https://en.wikipedia.org/wiki/LaTeX) markup.

## What is Golden Ratio?

Famously known as ***Phi*** that represents the Golden Ratio is an
irrational number that's approximately equal to ***1.6180*** and just like
it's cousin, ***Pi***, it has a never ending pattern of decimal digits.

\\[\Phi = 1.6180339887... \\]

According to the [article](https://en.wikipedia.org/wiki/Golden_ratio)
in Wikipedia, back in the Twentieth Century, architects and artists had
proportioned their works to approximate the Golden Ratio in the form of
a [Golden Rectangle](https://en.wikipedia.org/wiki/Golden_rectangle),
that is believed to be aesthetically pleasing.

## Time for some Calculus!

This is the equation used to find the ***n<sup>th</sup>*** Fibonacci Number:

\\[ F(n) = {log(\Phi)^n \over \sqrt{5}} \\]

Now, let's modify this formula to find the smallest integer i.e. the
first term of the 1000 digit number that fulfills this inequality:

\\[ {log(\Phi)^n \over \sqrt{5}} \gt {10^{999}} \\]

Expand the formula a little bit more:

\\[ n \times log(\Phi) - {log(5) \over 2} \gt {999 \times log(10)} \\]

\\[ n \times log(\Phi) \gt {999 \times log(10)} + {log(5) \over 2} \\]

We need to find n, so let's isolate it:

\\[ n = {{999 \times log(10) + {log(5) \over 2}} \over
{log(\Phi)}} = 4782.06 \\]

\\[ n \cong 4782 \\]


So, the first term that contains the 1000 digit Fibonacci Number is
***4782***.

Here's the solution using Python that solved in 0.000194 seconds:

```python
import math

limit = 999
golden_ratio = 1.6180

n = round(((limit * math.log(10)) + (math.log(5)/2))/(math.log(golden_ratio)))

print n
```

So, this is how it would look in our first equation above:

\\[F(4782) = {log(\Phi)^{4782} \over \sqrt{5}} = Some Large
Number \\]

Well, if you try to find the number using a calculator or compile it on
your computer, you'll end up having a compile error that says ***"Math
Error"***!

Hope you liked reading this article!

## References

+ [Fibonacci Number Sequence](https://en.wikipedia.org/wiki/Fibonacci_number)
+ [Golden Ratio](https://en.wikipedia.org/wiki/Golden_ratio)
+ [Golden Rectangle](https://en.wikipedia.org/wiki/Golden_rectangle)
