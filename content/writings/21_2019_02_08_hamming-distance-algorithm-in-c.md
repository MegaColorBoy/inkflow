title: Hamming Distance Algorithm in C++
date: December 18th, 2017
slug: hamming-distance-algorithm-in-c
category: Algorithms + Programming
summary: An article about the Hamming Distance algorithm that will be used in the next challenge.

This is a short article about the ***Hamming Distance*** algorithm, which will be used in The Cryptopals Crypto Challenges: Set 1 - Break Repeating-Key XOR challenge.

In [Challenge 6](http://cryptopals.com/sets/1/challenges/6), the first step states that you have to write a function to compute the ***edit distance/Hamming distance*** between two strings:

```text
this is a test
```

And

```text
wokka wokka!!!
```

When this function is executed, the expected result must be ***37***. If you we're able to make this function work, you can proceed with the next steps in the challenge.

## What is Hamming Distance?

Applied in domains like Cryptography, Information theory and Coding theory, Hamming distance is just the number of differing bits between two strings of equal length. Named after the American Mathematician, [Richard Hamming](https://en.wikipedia.org/wiki/Richard_Hamming), this algorithm mainly used for Error Detection and Error Correction (and yes, this also makes use of [Bitwise Operators](/posts/base64-encoding-decoding-using-bitwise-manipulation-in-c)).

Using the example above, let's see how this works, in theory:

```text
ASCII Format: this is a test
Binary Format: 011101[0][0] 01101[0][0][0] 011010[0]1 011[1][0]011 0[0]10000[0] 0[1]10[1]00[1] 01110[0]11 0[0]10[0][0][0][0] 0110[0]0[0]1 0[0]10[0]0[0][0] 011[1]0[1]0[0] 0[1]100[1]01 0[1]1[1]00[1]1 0[1]1[1]0[1]0[0]

ASCII Format: wokka wokka!!!
Binary Format: 011101[1][1] 01101[1][1][1] 011010[1]1 011[0][1]011 0[1]10000[1] 0[0]10[0]00[0] 01110[1]11 0[1]10[1][1][1][1] 0110[1]0[1]1 0[1]10[1]0[1][1] 011[0]0[0]0[1] 0[0]100[0]01 0[0]1[0]00[0]1 0[0]1[0]0[0]0[1]
```

As per the given example, when you count the number of differing bits (the bits marked in brackets) between the two strings, the result is ***37***.

With help of ***Google*** and ***Wikipedia***, I was able to build an implementation of this algorithm using the C++ programming language:

```cpp
//Hamming Distance
int CryptoLib::hamming_distance(string str1, string str2)
{
    int count=0;
    for(int i=0; i<str1.size(); i++)
    {
        int partial = (str1[i] & 0xFF) ^ (str2[i] & 0xFF);
        while(partial)
        {
            count += partial & 1;
            partial = partial >>1;
        }
    }
    return count;
}
```

***Note: This solution and the library named `crypto.h` was built using the C++ programming language. The source code for this solution can be found on Github.***

Hope you found this article useful!

Adios Amigo!