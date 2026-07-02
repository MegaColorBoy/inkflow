title: The Cryptopals Crypto Challenges: Set 1 - Detect Single-Character XOR
date: December 13th, 2017
slug: the-cryptopals-crypto-challenges-set-1--detect-singlecharacter-xor
category: Cryptography
summary: Write a method that derives which string that has a length of 60 characters has been encrypted using Single-Byte XOR cipher.

This is the [fourth challenge](http://cryptopals.com/sets/1/challenges/4) of Set 1 in The Cryptopals Crypto Challenges website. Previously, I spoke about these challenges and provided walkthroughs for the previous challenges, if you haven't read them, here are the links:

+ [The Cryptopals Crypto Challenges](/posts/the-cryptopals-crypto-challenges)
+ [The Cryptopals Crypto Challenges: Set 1 - Convert Hex to Base64](/posts/the-cryptopals-crypto-challenges-set-1--convert-hex-to-base64)
+ [Base64 Encoding / Decoding using Bitwise Manipulation in C++](/posts/base64-encoding-decoding-using-bitwise-manipulation-in-c)
+ [The Cryptopals Crypto Challenges: Set 1 - Fixed XOR Cipher](/posts/the-cryptopals-crypto-challenges-set-1--fixed-xor)
+ [The Cryptopals Crypto Challenges: Set 1 - Single-Byte XOR Cipher](/posts/the-cryptopals-crypto-challenges-set-1--singlebyte-xor-cipher)

For this challenge, given a [list](http://cryptopals.com/static/challenge-data/4.txt) of encrypted strings, you must derive which string (that has a length of 60 characters) is encrypted using ***Single-Byte XOR Cipher***.

Similar to the [previous post](/posts/the-cryptopals-crypto-challenges-set-1--singlebyte-xor-cipher), this is more about breaking the ***Single-Byte XOR Cipher*** technique. Remember, you can solve this challenge only if you were able to solve the previous challenge because you'll have to tweak some of the previous code in this challenge.

## How to detect Single-Byte XOR?

In the previous challenge, we're able to determine the key as we had one string but how do we do that with 300+ strings in a file except now that we also have to determine if the string is encrypted using ***Single-Byte XOR Cipher*** or not?

Here's comes the interesting part:

1.  Select the string that has the most english letters from the file
2.  Perform a Brute-force XOR on the string with the most english letters in which each character is XOR'd against every character from the ASCII table (256 characters)
3.  Pick the most english string after brute-forcing with each character
4.  Display the final result

Let's have a look at the code:

**Implementation of the method(s):**

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

//Return integer with the highest frequency of alphabets
int CryptoLib::high_frequency_count(map<char,int>m)
{
    int count = 0;
    for(auto p: m)
    {
        if(isalpha(p.first))
        {
            // cout << p.first << ":" << p.second << " ";
            count += p.second;
        }
    }
    return count;
}

//Detect string with Single Byte XOR
string CryptoLib::detectSingleByteXOR(vector<int> maxV)
{
    string final = "";
    int maxCount = 0;

    /*
        2. Perform a Brute-force XOR on the string that has
        the most english letters in which each character is XOR'd against
        every character from the ASCII table (256 characters)
    */
    for(int i=0; i<256; i++)
    {
        string temp = "";
        unsigned char a = i;
        for(int j=0; j<maxV.size(); j++)
        {
            unsigned char b = maxV[j];
            unsigned char c = b ^ a;
            temp += tolower(c);
        }

        //3. Select the string that has the most english letters. again.
        int count = high_frequency_count(frequency_table(temp));
        if(count > maxCount)
        {
            maxCount = count;
            final = temp;
        }
    }
    
    //4. Display the most "english" text as the final result
    return final;
}
```

**Final code:**

```cpp
//Cryptopals Set 1 Challenge 4
#include "crypto.h"

int main()
{
    CryptoLib crypt;

    ifstream infile;
    string str;
    int maxCount = 0;
    string maxString = "";
    vector<int> maxV;

    infile.open("enctext.txt");

    //if the file is not there
    if(!infile)
    {
        cout << "Unable to open the file";
        exit(1);
    }

    while(infile >> str)
    {
        //Only look for strings with 60 char length
        if(str.size() == 60)
        {
            str = crypt.add_spaces(crypt.con_hex_2_bin(str), 8);
            vector<int> v1 = crypt.con_bin_2_dec(str, 7.0);
            string newStr = crypt.con_dec_2_ascii(v1);

            //1. Select the string that has the most english letters
            int count = crypt.high_frequency_count(crypt.frequency_table(newStr));
            if(count > maxCount)
            {
                maxCount = count;
                maxString = newStr;
                maxV = v1;
            } 
        }
    }

    //2. Pass the list of decimals to the function (for now)
    cout << crypt.detectSingleByteXOR(maxV) << endl;
    return 0;
}
```

**Decrypted message:**

```text
Message: Now that the party is jumping.
```

***Note: This solution and the library named `crypto.h` was built using the C++ programming language. The source code for this solution can be found on Github.***

Stay tuned for the next challenge!