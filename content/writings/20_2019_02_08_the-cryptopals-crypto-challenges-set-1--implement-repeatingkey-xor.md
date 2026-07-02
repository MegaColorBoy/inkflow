title: The Cryptopals Crypto Challenges: Set 1 - Implement Repeating-Key XOR
date: December 15th, 2017
slug: the-cryptopals-crypto-challenges-set-1--implement-repeatingkey-xor
category: Cryptography
summary: Write a method that encrypts messages using the Repeating-Key XOR method with a given key.

This is the [fifth challenge](http://cryptopals.com/sets/1/challenges/5) of Set 1 in The Cryptopals Crypto Challenges website. Previously, I spoke about these challenges and provided walkthroughs for the previous challenges, if you haven't read them, here are the links:

+ [The Cryptopals Crypto Challenges](/posts/the-cryptopals-crypto-challenges)
+ [The Cryptopals Crypto Challenges: Set 1 - Convert Hex to Base64](/posts/the-cryptopals-crypto-challenges-set-1--convert-hex-to-base64)
+ [Base64 Encoding / Decoding using Bitwise Manipulation in C++](/posts/base64-encoding--decoding-using-bitwise-manipulation-in-c)
+ [The Cryptopals Crypto Challenges: Set 1 - Fixed XOR Cipher](/posts/the-cryptopals-crypto-challenges-set-1--fixed-xor)
+ [The Cryptopals Crypto Challenges: Set 1 - Single-Byte XOR Cipher](/posts/the-cryptopals-crypto-challenges-set-1--singlebyte-xor-cipher)
+ [The Cryptopals Crypto Challenges: Set 1 - Detect Single-Character XOR](/posts/the-cryptopals-crypto-challenges-set-1--detect-singlecharacter-xor)

For this challenge, you have to implement a ***Repeating-Key XOR*** method to encrypt the following message:

```text
Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal
```

With a given key:

```text
ICE
```

The final message should look like this:

```text
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
```

If you've already understood the concept of [XOR](/posts/base64-encoding-decoding-using-bitwise-manipulation-in-c) and had no issues implementing both [Fixed XOR Cipher](/posts/the-cryptopals-crypto-challenges-set-1--fixed-xor) and [Single-Byte XOR Cipher](/posts/the-cryptopals-crypto-challenges-set-1--singlebyte-xor-cipher), then this should be a piece of cake for you when it comes to implementing ***Repeating-Key XOR Cipher***.

## How does this work?

With ***Repeating-Key XOR***, you'll sequentially apply each byte of the key (which is "ICE", in this case); the first byte of plaintext will be XOR'd against ***"I"***, the next ***"C"***, the next ***"E"***, then ***"I"*** again for the 4th byte, and so on.

You can use this method to encrypt anything you want. Emails, Passwords, Secret messages and so on. You'll definitely get a feel for it because things will get interesting after this challenge.

Let's dive in to the code:

**Implementation of the method(s):**

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

//Repeating Key XOR implementation
string CryptoLib::repeatingKeyXOR(string str, string key)
{
    string newStr = "";
    int count = 0;

    /*
        1. Perform XOR against each character of the message 
        against each character of the key. 
        So if the key was "ICE" and the message is "abcdefg",
        it would be "a" against "I", then "b" against "C" and "c" against "E"
        but once it reaches the key's limit, you start again from the beginning
        of the key, which should be like: "d" against "I", "e" against "C" and so on.
    */
    for(int i=0; i<str.size(); i++)
    {
        unsigned char a = key[count];
        unsigned char b = str[i];
        unsigned char c = b ^ a;

        newStr += c;

        if(count == key.size()-1)
        {
            count = 0;
        }
        else
        {
            count++;
        }
    }

    //2. Convert the ASCII message to Hexadecimal
    string final = "0";
    final += con_ascii_2_hex(newStr);
    return final;
}
```

**Final code:**

```cpp
//Cryptopals Set 1 Challenge 5
#include "crypto.h"

int main()
{
    CryptoLib crypt;

    //Test cases provided
    string str = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal";
    string key = "ICE";

    cout << "ENCODED: " << crypt.repeatingKeyXOR(str, key) << endl;
    return 0;
}
```

***Note: This solution and the library named <mark>crypto.h</mark> was built using the C++ programming language. The source code for this solution can be found on Github.***

Stay tuned for the next challenge!