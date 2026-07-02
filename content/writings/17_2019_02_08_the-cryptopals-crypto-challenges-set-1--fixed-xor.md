title: The Cryptopals Crypto Challenges: Set 1 - Fixed XOR
date: December 12th, 2017
slug: the-cryptopals-crypto-challenges-set-1--fixed-xor
category: Cryptography
summary: Write a method that takes two strings of fixed equal length and produce their XOR combination.

This is the [second challenge](http://cryptopals.com/sets/1/challenges/2) of Set 1 in The Cryptopals Crypto Challenges website. Previously, I spoke about these challenges and provided a walkthrough for the first challenge, if you haven't read them, here are the links:

+ [The Cryptopals Crypto Challenges](/posts/the-cryptopals-crypto-challenges)
+ [The Cryptopals Crypto Challenges: Set 1 - Convert Hex to Base64](/posts/the-cryptopals-crypto-challenges-set-1--convert-hex-to-base64)
+ [Base64 Encoding / Decoding using Bitwise Manipulation in C++](/posts/base64-encoding--decoding-using-bitwise-manipulation-in-c)

For this challenge, you must write a method that takes two strings of fixed equal length and produce their XOR combination:

When you feed the following Hexadecimal string:

```text
1c0111001f010100061a024b53535009181c
```

And perform an XOR operation against another Hexadecimal string:

```text
686974207468652062756c6c277320657965
```

The method should return the following result:

```text
746865206b696420646f6e277420706c6179
```

Like the [first challenge](/posts/the-cryptopals-crypto-challenges-set-1-convert-hex-to-base64), this is sort of a warmup and a simple challenge to tackle. Just to give you a heads up, every challenge that you solve in this set would all make sense, in the end, as the challenges will get tougher and much more interesting.

## How do I solve this?

As I mentioned above, this problem is simple and pretty straightforward. In my previous post, I talked about Bitwise Manipulations and it's operators, I will be using the ***XOR (\^)*** operator, if you want to know more about it, [check out my previous post](/posts/base64-encoding--decoding-using-bitwise-manipulation-in-c). Also, I will reuse some of the functions that I had used in the **first challenge**. So let's dive in to the code:

**Methods that are being reused:**

```cpp
//Hashmap that contain hex key and binary values
map<char, string> CryptoLib::gen_hex_table()
{
    map<char, string> map;

    map['0'] = "0000";
    map['1'] = "0001";
    map['2'] = "0010";
    map['3'] = "0011";
    map['4'] = "0100";
    map['5'] = "0101";
    map['6'] = "0110";
    map['7'] = "0111";
    map['8'] = "1000";
    map['9'] = "1001";
    map['a'] = "1010";
    map['b'] = "1011";
    map['c'] = "1100";
    map['d'] = "1101";
    map['e'] = "1110";
    map['f'] = "1111";

    return map;
}

//Convert hex to string
string CryptoLib::con_hex_2_bin(string hexStr)
{
    map<char,string> m = gen_hex_table();

    string newStr = "";
    for(int i=0; i<hexStr.size(); i++)
    {
        if(isdigit(hexStr[i]))
        {
            newStr += m.find(hexStr[i])->second;
        }
        else
        {
            newStr += m.find(hexStr[i])->second;
        }
        // newStr += m.find(hexStr[i])->second;
    }
    return newStr;
}

//Convert binary to decimal
vector<int> CryptoLib::con_bin_2_dec(string str, double power)
{
    vector<int> v;
    string newStr = "";
    istringstream iss(str);
    string x;

    while(iss >> x)
    {
        double p = power;
        double decimal = 0.0;

        for(int i=0; i<x.size(); i++)
        {
            if(x[i] == '1')
            {
                decimal += pow(2.0, p);
            }
            p--;
        }
        v.push_back((int)decimal);
    }
    return v;
}

//Add spaces between strings
string CryptoLib::add_spaces(string str, int spaces)
{
    string newStr = "";
    int count = 0;

    for(int i=0; i<str.size(); i++)
    {

        // newStr += str[i];
        if(count == spaces)
        {
            newStr += " ";
            i--;
            count = 0;
        }
        else
        {
            newStr += str[i];
            count++;
        }
    }

    return newStr;
}

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
```

**Implementation of the method:**

```cpp
//Fixed XOR implementation
string CryptoLib::fixedXOR(string str1, string str2)
{
    //Check if the length of both the strings are equal
    if(str1.size() != str2.size())
    {
        return "The strings are not of equal length.";
    }
    else
    {
        string newStr = "";

        //Step 1. convert hex to binary of 8 bits
        str1 = add_spaces(con_hex_2_bin(str1), 8);
        str2 = add_spaces(con_hex_2_bin(str2), 8);

        //Step 2. convert binary to decimal
        vector<int> v1 = con_bin_2_dec(str1, 7.0);
        vector<int> v2 = con_bin_2_dec(str2, 7.0);

        //Step 3. XOR the decimals of v1 with decimals of v2
        for(int i=0; i<v1.size(); i++)
        {
            //Get the char of the first string
            unsigned char a = v1[i];

            //Get the char of the second string
            unsigned char b = v2[i];
            
            //Perform XOR operation against each other
            unsigned char c = a ^ b;

            //Concatenate the string
            newStr += c;
        }

        //ASCII result: the kid don't play.

        //Final result - Convert the ASCII string to Hexadecimal
        return con_ascii_2_hex(newStr); 
    }
}
```

**Final code:**

```cpp
//CryptoPals Set 1 Challenge 2
#include "crypto.h"

int main()
{
    CryptoLib crypt;

    //The test cases provided
    string str1 = "1c0111001f010100061a024b53535009181c";
    string str2 = "686974207468652062756c6c277320657965";

    cout << crypt.fixedXOR(str1, str2) << endl;
    return 0;
}
```

***Note: This solution and the library named `crypto.h` was built using the C++ programming language. The source code for this solution can be found on Github.***

Stay tuned for the next challenge!