title: The Cryptopals Crypto Challenges: Set 1 - Break Repeating-Key XOR
date: December 18th, 2017
slug: the-cryptopals-crypto-challenges-set-1--break-repeatingkey-xor
category: Cryptography
summary: Write a method that decodes a message which is encrypted using the Repeating-Key XOR cipher.

This is the [sixth challenge](http://cryptopals.com/sets/1/challenges/6) of Set 1 in The Cryptopals Crypto Challenges website. Previously, I spoke about these challenges and provided walkthroughs for the previous challenges, if you haven't read them, here are the links:

+ [The Cryptopals Crypto Challenges](/posts/the-cryptopals-crypto-challenges)
+ [The Cryptopals Crypto Challenges: Set 1 - Convert Hex to Base64](/posts/the-cryptopals-crypto-challenges-set-1--convert-hex-to-base64)
+ [Base64 Encoding / Decoding using Bitwise Manipulation in C++](/posts/base64-encodingdecoding-using-bitwise-manipulation-in-c)
+ [The Cryptopals Crypto Challenges: Set 1 - Fixed XOR Cipher](/posts/the-cryptopals-crypto-challenges-set-1--fixed-xor)
+ [The Cryptopals Crypto Challenges: Set 1 - Single-Byte XOR Cipher](/posts/the-cryptopals-crypto-challenges-set-1--singlebyte-xor-cipher)
+ [The Cryptopals Crypto Challenges: Set 1 - Detect Single-Character XOR](/posts/the-cryptopals-crypto-challenges-set-1--detect-singlecharacter-xor)
+ [The Cryptopals Crypto Challenges: Set 1 - Implement Repeating-Key XOR](/posts/the-cryptopals-crypto-challenges-set-1--implement-repeatingkey-xor)
+ [Hamming Distance Algorithm in C++](/posts/hamming-distance-algorithm-in-c)

For this challenge, you are given a [file](http://cryptopals.com/static/challenge-data/6.txt), which contains a ciphertext that has been encrypted using [Repeating-Key XOR](/posts/the-cryptopals-crypto-challenges-set-1--implement-repeatingkey-xor) and then encoded using Base64. Decrypt it.

According to the problem description on the website:

> It is officially on, now.
>
> This challenge isn't conceptually hard, but it involves actual
> error-prone coding. The other challenges in this set are there to
> bring you up to speed. This one is there to qualify you. If you can do
> this one, you're probably just fine up to Set 6.

Well, conceptually, this may not be the hardest but practically, it is the first hardest challenge in this set and it really did take me a while to understand how to decrypt the ciphertext through ***trial-and-error*** despite the instructions given on the website. In this challenge, it's more like connecting all the puzzles and looking at the big picture, in this case, all of the previous code that I had written, is to break the Repeating-Key XOR cipher.

## How to break it?

The challenge had given some steps to follow. Here's how:

1.  Let ***KEYSIZE*** be the guessed length of the key; try values from 2 to (say) 40
2.  Write a function to compute the edit distance/Hamming distance between two strings. To know more about it, [click here](/posts/hamming-distance-algorithm-in-c) 
3.  For each ***KEYSIZE***, take the first ***KEYSIZE*** worth of bytes, and the second ***KEYSIZE*** worth of bytes, and find the edit distance between them. Normalize this result by dividing by ***KEYSIZE***
4.  The ***KEYSIZE*** with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 ***KEYSIZE*** values. Or take 4 ***KEYSIZE*** blocks instead of 2 and average the distances
5.  Now that you probably know the ***KEYSIZE***: break the ciphertext into blocks of ***KEYSIZE*** length
6.  Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on
7.  Solve each block as if it was single-character XOR. You already have code to do this
8.  For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key

Let's dive in to the code (I hope the comments, help you out!):

**Implementation of the method(s):**

```cpp
//Single Byte XOR V2 - a better version
string CryptoLib::singleByteXOR_V2(string str, char key)
{
    //Don't forget to add a NULL character to the string, it broke when I didn't add it previously.
    string newStr(str.size(),''); 
    
    for(int i=0; i&lt;str.size(); ++i){
        newStr[i] = str[i] ^ key;
    }
    return newStr;
}

//Return the Single Byte XOR key via Bruteforce
char CryptoLib::singleByteXOR_Bruteforce_key(string cipherBlock)
{
    char key = 0;
    int maxCount=0;
    string decodedMessage;

    //Brute force all 256 possibilities
    for(int i=0; i<=256; i++)
    {
        char ch = (char) i;

        //Perform Single Byte XOR -- modified version
        string attempt = singleByteXOR_V2(cipherBlock, ch);

        // cout << "Message: " << attempt << endl;

        int count = 0;
        /*
            Look for characters that are alphabetic and the space character,
            if it finds, increment the counter
        */
        for(int j=0; j&lt;attempt.size(); j++)
        {
            if((attempt[j] >= 65 && attempt[j] <= 122) || attempt[j] == ' ')
            {
                count++;
            }
        }

        //The one with the highest count, has the predicted key
        if(count > maxCount)
        {
            maxCount = count;
            key = ch;
            // decrypted = attempt;
        }
    }

    // cout << "KEY: " << key << endl;
    // cout << "MESSAGE: " << decrypted << endl;

    return key;
}

//Guess Key length of the cipher
int CryptoLib::guess_key_length(string cipherText)
{
    int KEYSIZE = -1;
    double leastNormalized = INT_MAX;
    
    //Guess a keysize from 2 to 40
    for(int i=2; i<=40; i++)
    {
        double normalize = 0.0f;

        //Number of bytes per key size
        int bytes = cipherText.size()/i;

        for(int j=0; j&lt;bytes; j++)
        {
            string blockA = cipherText.substr((j*i), i);
            string blockB = cipherText.substr(((j+1)*i), i);
        
            //Calculate Hamming Distance between 2 strings
            int edit_distance = hamming_distance(blockA, blockB);

            normalize += ((double)edit_distance)/((double)blockA.size());
        }

        //Now, take an average 
        normalize /= bytes;

        //The key size that has the least edit distance is the key size required
        if(normalize > 0 && normalize < leastNormalized)
        {
            leastNormalized = normalize;
            KEYSIZE = i;
        }
    }

    //Return the key size
    return KEYSIZE;
}
```

**Final code:**

```cpp
//The Cryptopals Crypto Challenges - Set 1 Challenge 6
#include "crypto.h"

int main()
{
    CryptoLib crypt;
    string message;
    string binary;
    string key;

    //if this returns 37, then the function is working correct!
    // cout << crypt.hamming_distance("this is a test", "wokka wokka!!!") << endl;

    //Read the file content
    ifstream infile;

    //Converted the B64 text to Hexadecimals through an online converter
    //as it wasn't accurate with b64 decoder that I'd built
    infile.open("message.txt");
    getline(infile, message, '');
    infile.close();

    //Convert the hexadecimal string to ASCII
    message = crypt.con_hex_2_ascii(message);

    //Guess the length of the key
    int keyLength = crypt.guess_key_length(message);

    //Transpose the message based on keysize length
    int blocks = message.size() / keyLength;

    for(int i=0; i&lt;keyLength; ++i)
    {
        string block;
        char indexKey='';
 
        /*
            Transpose the message into blocks 
            based on keysize and concatenate it 
            into one string
        */
        for(int j=0; j&lt;blocks; j++){
            block += message.substr((j*keyLength) + i,1);
        }

        //Concatenate the selected characters, which will become the predicted key
        key += crypt.singleByteXOR_Bruteforce_key(block);
    }

    cout << "KEY: " << key << endl;
    cout << "DECODED: " << crypt.con_hex_2_ascii(crypt.repeatingKeyXOR(message, key)) << endl;

    return 0;   
}
```

***Note: This solution and the library named `crypto.h` was built using the C++ programming language. The source code for this solution can be found on Github.***

When the following code is executed, the most probable ***KEYSIZE*** is ***29*** and after transposing the message and decrypting the blocks, you get a key of that length:

```text
Terminator X: Bring the noise
```

Lastly, use the ***Repeating-Key XOR*** method to decrypt the message with the cracked key (which looks like lyrics to some music track!):

```text
A rockin' on the mike while the fly girls yell
Well that's my DJ Deshay cuttin' all them Z's
Vanilla's on the mike, man I'm not lazy. ?I'm lettin' my drug kick in
To just let it flow, let my concepts go
And if you don't give a damn, then
So get off 'cause I control the stage
I'm in my own phase
And I can dance better than any kid n' play ?
Stage 2 -- Yea the one ya' wanna listen to
So I can funk it up and make it sound good
For good luck, I like my rhymes atrocious
I'm an effect and that you can bet
There's no denyin', You can try to hang 
Over and over, practice makes perfect
Soon -- Oh my God, homebody, you probably eat
Intoxicating so you stagger like a wino
Vanilla Ice is sellin' and you people are buyin'
Movin' and groovin' trying to sing along
Now you're amazed by the VIP posse. ?
Steppin' so hard like a German Nazi
There's no trippin' on mine, I'm just gettin' down
You trapped me once and I thought that
So step down and lend me your ear 
Your body's gettin' hot, so, so I can smell it
'Cause the lyrics belong to ICE, You can call me Dad 
Let the witch doctor, Ice, do the dance to cure 
You wanna battle me -- Anytime, anywhere ?
You thought that I was weak, Boy, you're dead wrong 
play that funky music Go white boy, go white boy, go
Play that funky music white boy you say it, say it 
Play that funky music, white boy Come on, Come on, Come on
```

As mentioned above, this was really challenging and fun, at the same time. Although, Most people (academically) know ***"how-to"*** break a Repeating-Key XOR (Vignere Cipher) but being ***able*** to break it, is another thing.

Hope you liked reading this article!

But, hang in there, surprisingly, this code will be useful later on for many problems.