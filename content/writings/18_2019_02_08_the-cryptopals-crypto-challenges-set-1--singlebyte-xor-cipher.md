title: The Cryptopals Crypto Challenges: Set 1 - Single-Byte XOR Cipher
date: December 13th, 2017
slug: the-cryptopals-crypto-challenges-set-1--singlebyte-xor-cipher
category: Cryptography
summary: Write a method that decrypts a hexadecimal message that has been XOR'd against a single character.

This is the [third challenge](http://cryptopals.com/sets/1/challenges/3) of Set 1 in The Cryptopals Crypto Challenges website. Previously, I spoke about these challenges and provided walkthroughs for the previous challenges, if you haven't read them, here are the links:

+ [The Cryptopals Crypto Challenges](/posts/the-cryptopals-crypto-challenges)
+ [The Cryptopals Crypto Challenges: Set 1 - Convert Hex to Base64](/posts/the-cryptopals-crypto-challenges-set-1--convert-hex-to-base64)
+ [Base64 Encoding / Decoding using Bitwise Manipulation in C++](/posts/base64-encoding--decoding-using-bitwise-manipulation-in-c)
+ [The Cryptopals Crypto Challenges: Set 1 - Fixed XOR Cipher](/posts/the-cryptopals-crypto-challenges-set-1--fixed-xor)

For this challenge, you have to write a method that decodes a
Hexadecimal string:

```text
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
```

That has been ***XOR'd*** against a ***single character***. You must find the key and decrypt the message.

If you have read the [previous article](/posts/the-cryptopals-crypto-challenges-set-1--fixed-xor), it was clearly setup for this problem. There are so many ways to solve this problem but the most efficient way to solve it is by using a ***Frequency table***.

Assuming the message is supposed to be in English, when decrypted, we need to only generate a frequency table using the given Hexadecimal string that shows the frequencies of each ***alphabet***. The character that has the highest frequency is the key required, which is then used to perform an ***XOR (\^)*** operation against each character, to decrypt the encrypted message.

Let's have a look at the code:

```cpp
//Return Character frequency of a string
map<char, int> CryptoLib::frequency_table(string str)
{
    map<char, int> m;
    map<char, int>::iterator it;

    for(int i=0; i<str.size(); i++)
    {
        char ch = str[i];
        it = m.find(ch);

        if(it == m.end())
        {
            m.insert(make_pair(ch,1));
        }
        else
        {
            it->second++;
        }
    }

    return m;
}

//Return character with the highest frequency
char CryptoLib::ret_high_freq_char(map<char, int> m)
{
    int max_count = 0;
    char max_char;

    for(auto p: m)
    {
        if(isalpha(p.first))
        {
            if(p.second > max_count)
            {
                max_char = p.first;
                max_count = p.second;
            }
        }
    }
    return max_char;
}

//Single Byte XOR
string CryptoLib::singleByteXOR(string str)
{
    string newStr = "";

    //1. Convert Hexadecimal to Binary
    str = add_spaces(con_hex_2_bin(str), 8);

    //2. Convert Binary to Decimals
    vector<int> v = con_bin_2_dec(str, 7.0);

    
    // What's happening here?
    // 4. Generate a frequency table using the characters from the ASCII string
    // 5. Look for characters that are English and also has the highest frequency
    // 6. The character that has the highest frequency is the KEY!
    
    //The key
    unsigned char a = toupper(ret_high_freq_char(frequency_table(con_dec_2_ascii(v))));

    //7. Perform XOR with the KEY against each character
    for(int i=0; i<v.size(); i++)
    {
        unsigned char b = v[i];
        unsigned char c = b ^ a;
        newStr += c;
    }

    //8. Decoded message
    return newStr;
}
```

**Final code:**

```cpp
//CryptoPals Set 1 Challenge 3
#include "crypto.h"

int main()
{
    CryptoLib crypt;

    //Test case provided
    string str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736";
    cout << "DECODED: " << crypt.singleByteXOR(str) << endl;
    return 0;
}   
```

**Decrypted message:**

```text
Key with the highest frequency: 'X'
Message: Cooking MC's like a pound of bacon
```

***Note: This solution and the library named `crypto.h` was built using the C++ programming language. The source code for this solution can be found on Github.***

Stay tuned for the next challenge!