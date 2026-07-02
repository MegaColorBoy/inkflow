title: Base64 Encoding / Decoding using Bitwise Manipulation in C++
date: December 11th, 2017
slug: base64-encoding--decoding-using-bitwise-manipulation-in-c
category: Algorithms + Programming
summary: An alternate solution to the previous post on how to encode/decode hexadecimals to Base64 and vice-versa using Bitwise Manipulation.

In the [previous post](/posts/the-cryptopals-crypto-challenges-set-1--convert-hex-to-base64), I provided the walkthrough for the first challenge of Set 1 in The Cryptopals Crypto Challenges website but then I realized that I didn't write a method that could decode the Base64 string back to it's original Hexadecimal format. So I went back to the website again and found an important rule that I should have not ignored, at the very beginning:

> Cryptopals Rule:
>
> Always operate on raw bytes, never on encoded strings. Only use Hex
> and Base64 for pretty-printing.

Although, the solution I had provided in the first one works, but there's no way that I could go back to displaying the original Hexadecimal string. So I went on **Wikipedia** and did some research on Base64 and I figured out that I should brush up my knowledge on [Bitwise Manipulation](https://en.wikipedia.org/wiki/Bit_manipulation) as I never had a use for it until now.

In this post, which should be pretty much straightforward (and probably longer too), I will be talking about Bitwise Manipulation and it's operators and also provide an alternate walkthrough for the first challenge of The Cryptopals Crypto Challenges.

## What is Bitwise Manipulation?

Bitwise Manipulation is a low-level, algorithmic technique used to manipulate bits or data that are shorter than a word. This technique is mostly used on embedded controls, data compression, encryption algorithms and error-detection.

As I mentioned above, most programmers don't get to use this technique a lot as most programming languages allows the programmer to work on abstractions directly instead of bits that represent those abstractions.

A program that implements bitwise manipulation, makes use of the following operators:

+ Bit Shifts (<< / >>)
+ AND (&)
+ OR (|)
+ NOT (!)
+ XOR (\^)

### Bit Shift operations

Let's take a look at both the left ***<<*** and right ***>>*** shift operators. So if you use either of them, you would be shifting ***x*** number of bits to left or right in a variable.

Let's say we have the number ***x = 4***, and it's binary form is ***00000100*** and we wanted to shift by 4 bits to the left, we just have to call ***x << 4***, the result would be ***00100000***, which means ***x = 64***. Shifting to the left is the equivalent of multiplication by the power of ***n*** because ***4x2^4^ = 64***. Similarly, shifting to the right is the equivalent of division by the power of ***n*** because ***4 / 2^4^ = 4*** and it's binary form would be ***00000100***.

### AND, OR and NOT operations

The bitwise operator **AND** is useful, when you want to check a bit is on or off i.e. ***0*** or ***1***. Whereas for the bitwise operator **OR** is the exact opposite, if either bit is on, then the result will be ***1***, else it will be ***0***. Finally, the bitwise operator **NOT** is used for inverting the bits in a binary, for example, if you had a binary string of ***00101000***, you'd get ***11010111***, it is used best when you want to turn off a bit combined with the **AND** operator.

### XOR operator

Relax, this ain't scary, this is also known as **Exclusive-OR**. This operator works when both bits that are compared are either ***0*** or ***1***, then the result will be ***0***, else it will be ***1***. So if you perform an XOR on ***01001000*** and ***01000100***, the result will be ***00001100***.

I hope that by now, you must have understood the basic concept of Bitwise Manipulation, if not, then spend some time reading about it before scrolling down to the next topic i.e. on how it's applied to encode and decode Hexadecimal strings to Base64 strings and vice-versa.

## Base64 Encoding

Before you get started, please keep a couple of things in your mind:

+ Each Hexadecimal character has 4 bits (Base 16)
+ Each Base64 character has 6 bits (Base 32)
+ We will be using the standard MIME-Base64 Encoding, thus we will have to use ***'+'*** and ***'/'*** characters as well

Now that we have the facts, doing a simple math states that every 3 Hexadecimal characters is equal to 2 Base64 characters, since the least common multiple between 4 and 6 is 12. In order to do this, we are going to make use of our Bitwise Operators, let's have a look at the method:

```cpp
//Base64 Encoder
string CryptoLib::b64_encode(string str)
{
    string newStr = "";
    string ref = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    
    //Number of bytes per 12 bits
    int bytes = str.size() / 3;
    int padding = str.size() % 3;

    //Padding must be either 0 or 1
    if(padding > 1)
    {
        return newStr;
    }

    //Number of characters to be encoded is 3

    int count = bytes * 3;

    unsigned long long h = 0;

    int i = 0;
    for(i=0; i<count; i+=3) //iterate every 3 chars
    {
        //Get every 3 chars
        char a[2] = {str[i], 0};
        char b[2] = {str[i+1], 0};
        char c[2] = {str[i+2], 0};

        //Now, convert each hex character (base 16) to it's equivalent decimal number
        //and merge them into one variable
        h = strtoull(a, nullptr, 16) << 8; //shift left by 8 bits
        h |= strtoull(b, nullptr, 16) << 4; //shift left by 4 bits
        h |= strtoull(c, nullptr, 16); //no shift required only the first 2 characters need
    
        //HEX: 0x3F -> DEC: 63 -> ASCII: ?

        newStr += ref[0x3F & (h >> 6)]; //first b64 char; shift to right by 6 bits
        newStr += ref[0x3F & h]; //second b64 char
    }

    //if padding is required
    //Follows the same pattern as the above.
    if(padding == 1)
    {
        char a[2] = {str[i], 0};
        h = strtoull(a, nullptr, 16) << 8; // shift left by 8 bits
        newStr += ref[0x3F & (h >> 6)];
        newStr += '='; //add this towards the end of the encoded string
    }

    return newStr;
}
```

If you're wondering on how to convert an ASCII string, all you have to do is convert the ASCII string to a Hexadecimal string and then use this method to give you the Base64 encoded string.

## Base64 Decoding

What if you wanted to get back to the original string? Well, that's what we are going to do next. Unlike the previous post, you might have noticed that I didn't use any Hashmaps for encoding the Base64 characters, I wanted to try a different approach and also thought of increasing speed and efficiency and of course, keeping it simple.

Let's take a look at the method:

```cpp
//Base64 Decoder
string CryptoLib::b64_decode(string str)
{
    string newStr = "";
    string ref = "0123456789abcdef";

    //Check if this is a valid b64 string
    if(str.size() % 2 != 0)
    {
        return newStr;
    }

    //Number of bytes for hexadecimals
    int bytes = str.size() / 2;
    int count = bytes build.sh content convert.sh make_entry.py output ssg.py ssg.pyc templates transfer.sh venv 2;

    unsigned long long h = 0;
    for(int i=0; i<count; i+=2) //iterate every 2 chars
    {
        for(int j=0; j<2; j++)
        {
            h <<= 6; //shift 6 bits to the left

            //Check if the value is in the range of A-Z
            if(str[i+j] >= 0x41 && str[i+j] <= 0x5a)
            {
                h |= str[i+j] - 0x41;
            }
            //Check if the value is in the range of a-z
            else if(str[i+j] >= 0x61 && str[i+j] <= 0x7a)
            {
                h |= str[i+j] - 0x47;
            }
            //Check if the value is in the range of 0-9
            else if(str[i+j] >= 0x30 && str[i+j] <= 0x39)
            {
                h |= str[i+j] + 0x04;
            }
            //Check if the value is a '+'
            else if(str[i+j] == 0x2b)
            {
                h |= 0x3e;
            }
            //Check if the value is a '/'
            else if(str[i+j] == 0x2f)
            {
                h |= 0x3f;
            }
            //Check if the value is a '='
            else if(str[i+j] == 0x3d)
            {
                if(count - (i+j) == 1)
                {
                    newStr += ref[0xf & (h >> 8)];
                }
            }
        }
        //Shift to the right by 8 bits
        newStr += ref[0xf & (h >> 8)];
        //Shift to the right by 4 bits
        newStr += ref[0xf & (h >> 4)];
        newStr += ref[0xf & h];
    }

    return newStr;
}
```

In the final code, I just converted an ASCII string to Base64 string, let's have a look at it:

**Methods to convert ASCII string to Hexadecimal string and vice-versa:**

```cpp
//Convert ASCII to HEX
string CryptoLib::con_ascii_2_hex(string str)
{
    stringstream ss;
    for(int i=0; i<str.size(); i++)
    {
        ss << std::hex << (int)str[i];
    }
    return ss.str();
}

//Convert HEX to ASCII
string CryptoLib::con_hex_2_ascii(string str)
{
    string newStr = "";
    str = add_spaces(con_hex_2_bin(str), 8);
    vector v = con_bin_2_dec(str, 7.0);

    for(int i=0; i<v.size(); i++)
    {
        newStr += (char)v[i];
    }
    return newStr;
}
```

**Final Code:**

```cpp
//CryptoPals Set 1 Challenge 1
#include "crypto.h"

int main()
{
    CryptoLib crypt;

    string str = crypt.con_ascii_2_hex("Hello World");
    string enc = crypt.b64_encode(str); 
    cout << "ENCODED: " << enc << endl;

    string dec = crypt.con_hex_2_ascii(crypt.b64_decode(enc));
    cout << "DECODED: " << dec << endl;
    return 0;
}
```

***Note: This solution and the library named `crypto.h` was built using the C++ programming language. The source code for this solution can be found on Github.***

Hope you guys liked reading this article!

Until next time, then!