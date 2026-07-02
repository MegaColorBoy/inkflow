title: The Cryptopals Crypto Challenges: Set 1 - Convert Hex to Base64
date: December 6th, 2017
slug: the-cryptopals-crypto-challenges-set-1--convert-hex-to-base64
category: Cryptography
summary: Convert Hexadecimal strings to encoded Base64 strings.

This is the [first challenge](http://cryptopals.com/sets/1/challenges/1) of Set 1 in The Cryptopals Crypto Challenges website. If you want to know more about these challenges, look at my [previous post](/posts/the-cryptopals-crypto-challenges).

For this challenge, you need to be able to convert Hexadecimal strings to encoded Base64 strings:

The string:

```text
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
```

Should produce:

```text
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
```

Not only is this challenge just a warmup but it is also designed to make you feel comfortable in dealing with raw bytes as Base64 is used to encode binary information and Hexadecimal is used to view the raw bytes.

## How to convert from Hexadecimal to Base64?

Well, it's simpler than you think! You will have to go through the following steps:

1.  [Convert hexadecimal string to binary string](#step-1)
2.  [Split the binary string into 4 pieces of 6 bits each](#step-2)
3.  [Convert the binary string to decimal](#step-3)
4.  [Compare each decimal against each character in a reference string of 64 characters](#step-4)

### <a id="step-1"></a> Convert hexadecimal string to binary string

Before converting to binary, you should compare each character against a hashmap table of hardcoded hexadecimal keys and binary values.

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
    for(int i=0; i <hexStr.size(); i++)
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
```

### <a id="step-2"></a> Split the binary string into 4 pieces of 6 bits each

Base64 represents data in the form of ASCII format that follows a Radix-64 representation. Each character is picked from a set of 64 characters, which means that I'll only need 6 bits represent each character because **2<sup>6</sup> = 64 characters**.

```cpp
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
```

### <a id="step-3"></a> Convert the binary string to decimal

Before converting, you should know that a decimal number is equal to the sum of binary digits (d~n~) times their power of 2 (2<sup>n</sup>).

Let's say you have a binary string of <mark>111001</mark>, it's decimal
would be <mark>1x2<sup>5</sup> + 1x2<sup>4</sup> + 1x2<sup>3</sup> + 0x2<sup>2</sup> + 0x2<sup>1</sup> + 1x2<sup>0</sup> =
57</mark>

```cpp
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
```

### <a id="step-4"></a> Compare each decimal against each character in a reference string of 64 characters

At this stage, all you have to do is find and concatenate each character (using the reference string) based on each decimal and return your encoded Base64 string as the final output.

```cpp
//Convert HEX to Base 64
string CryptoLib::con_hex_2_b64(string str)
{
    string b64 = "";
    string ref = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    string newStr = add_spaces(con_hex_2_bin(str), 6);

    vector<int> v = con_bin_2_dec(newStr, 5.0);

    for(int i=0; i<v.size(); i++)
    {
        b64 += ref[v[i]];
    }

    return b64;
}
```

Here's the final section of the code:

```cpp
//CryptoPals Set 1 Challenge 1
#include "crypto.h"

int main()
{
    CryptoLib crypt;

    //Test case provided from the site
    string str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
    cout << crypt.con_hex_2_b64(str) << endl;
    return 0;
}
```

***Note: This solution and the library named `crypto.h` was built using the C++ programming language. The source code for this solution can be found on Github.***

Stay tuned for the next challenge.