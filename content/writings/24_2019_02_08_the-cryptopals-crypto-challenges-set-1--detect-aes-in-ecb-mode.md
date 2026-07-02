title: The Cryptopals Crypto Challenges: Set 1 - Detect AES in ECB Mode
date: December 29th, 2017
slug: the-cryptopals-crypto-challenges-set-1--detect-aes-in-ecb-mode
category: Cryptography
summary: Find the string that has been encrypted with AES-128 cipher with an ECB mode in a file of ciphertexts.

This is the [eighth challenge](http://cryptopals.com/sets/1/challenges/8) of Set 1 in The Cryptopals Crypto Challenges website. Previously, I spoke about these challenges and provided walkthroughs for the previous challenges, if you haven't read them, here are the links:

+ [The Cryptopals Crypto Challenges](/posts/the-cryptopals-crypto-challenges)
+ [The Cryptopals Crypto Challenges: Set 1 - Convert Hex to Base64](/posts/the-cryptopals-crypto-challenges-set-1-convert-hex-to-base64)
+ [Base64 Encoding / Decoding using Bitwise Manipulation in C++](/posts/base64-encoding-decoding-using-bitwise-manipulation-in-c)
+ [The Cryptopals Crypto Challenges: Set 1 - Fixed XOR Cipher](/posts/the-cryptopals-crypto-challenges-set-1-fixed-xor)
+ [The Cryptopals Crypto Challenges: Set 1 - Single-Byte XOR Cipher](/posts/the-cryptopals-crypto-challenges-set-1-single-byte-xor-cipher)
+ [The Cryptopals Crypto Challenges: Set 1 - Detect Single-Character XOR](/posts/the-cryptopals-crypto-challenges-set-1-detect-single-character-xor)
+ [The Cryptopals Crypto Challenges: Set 1 - Implement Repeating-Key XOR](/posts/the-cryptopals-crypto-challenges-set-1-implement-repeating-key-xor)
+ [Hamming Distance Algorithm in C++](/posts/hamming-distance-algorithm-in-c)
+ [The Cryptopals Crypto Challenges: Set 1 - Break Repeating-Key XOR](/posts/the-cryptopals-crypto-challenges-set-1-break-repeating-key-xor)
+ [The Cryptopals Crypto Challenges: Set 1 - AES in ECB Mode](/posts/the-cryptopals-crypto-challenges-set-1-aes-in-ecb-mode)

For this challenge, you are given a [file](http://cryptopals.com/static/challenge-data/8.txt), which contains a bunch of ciphertexts that has been encrypted using ***AES-128 Cipher*** but only one of them has an ***ECB (Electronic Codebook)*** mode. Find the string the string that has the ECB mode.

In the [previous post](/posts/the-cryptopals-crypto-challenges-set-1-aes-in-ecb-mode), I had explained that ***ECB*** is a cipher mode that is used to repeat the key until it covers the entire plaintext i.e. the same 16 byte plaintext will have the same 16 byte ciphertext.

Well, the solution is pretty much trivial, so here's the solution:

**Implementation of the method(s):**

```cpp
//Detect ECB Mode in AES Cipher
bool CryptoLib::detect_ecb_mode(string str, int keyLength)
{
    //Divide into equal amount of blocks
    int blocks = str.size() / keyLength;

    /*
        Theory: the problem with ECB as I had mentioned
        in the previous post, it uses the exact number of bytes of the ciphertext
        to encrypt the plaintext repeatedly.

        In that case, just do the reverse.

        Divide it into equal amount of blocks, in this case, we
        know the key is "YELLOW SUBMARINE", which is 16 bytes.

        Then, all you have to do is take two substrings of a string and compare,
        if they have the same string, we found it!
    */
    for(int i=0; i<blocks; i++)
    {
        //Take a substring of x number of bytes
        string strA = str.substr(i*keyLength, keyLength);

        for(int j=i+1; j<blocks; j++)
        {
            //Take another substring of x number of bytes
            string strB = str.substr(j*keyLength, keyLength);
            if(strA == strB)
            {
                //Found
                return true;
            }
        }
    }
    return false;
}
```

**Final code:**

```cpp
//The Cryptopals Crypto Challenges - Set 1 Challenge 8
#include "crypto.h"

int main()
{
    CryptoLib crypt;

    string str;

    ifstream infile;
    infile.open("8.txt");

    int count = 0;
    while(!infile.eof())
    {
        getline(infile, str);

        //Check if this string has ECB mode
        if(crypt.detect_ecb_mode(str, 16) == true)
        {
            cout << "FOUND AT LINE " << count << " => " << str << endl;
            break;
        }
        count++;
    }
}
```

***Note: This solution and the library named <mark>crypto.h</mark> was
built using the C++ programming language. The source code for this
solution can be found on Github.***

Well, this challenge marks the end of Set 1 from The Cryptopals Crypto
Challenges. However, I do intend to continue solving all these crypto
challenges, let's see how it goes!

Until next time, then!