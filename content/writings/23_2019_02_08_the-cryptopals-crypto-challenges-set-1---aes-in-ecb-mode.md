title: The Cryptopals Crypto Challenges: Set 1 -  AES in ECB Mode
date: December 21st, 2017
slug: the-cryptopals-crypto-challenges-set-1---aes-in-ecb-mode
category: Cryptography
summary: Decrypt a Base64 encoded file that is encrypted with an AES-128 Cipher in ECB mode.

This is the [seventh challenge](http://cryptopals.com/sets/1/challenges/7) of Set 1 in The Cryptopals Crypto Challenges website. Previously, I spoke about these challenges and provided walkthroughs for the previous challenges, if you haven't read them, here are the links:

+ [The Cryptopals Crypto Challenges](/posts/the-cryptopals-crypto-challenges)
+ [The Cryptopals Crypto Challenges: Set 1 - Convert Hex to Base64](/posts/the-cryptopals-crypto-challenges-set-1-convert-hex-to-base64)
+ [Base64 Encoding / Decoding using Bitwise Manipulation in C++](/posts/base64-encoding-decoding-using-bitwise-manipulation-in-c)
+ [The Cryptopals Crypto Challenges: Set 1 - Fixed XOR Cipher](/posts/the-cryptopals-crypto-challenges-set-1-fixed-xor)
+ [The Cryptopals Crypto Challenges: Set 1 - Single-Byte XOR Cipher](/posts/the-cryptopals-crypto-challenges-set-1-single-byte-xor-cipher)
+ [The Cryptopals Crypto Challenges: Set 1 - Detect Single-Character XOR](/posts/the-cryptopals-crypto-challenges-set-1-detect-single-character-xor)
+ [The Cryptopals Crypto Challenges: Set 1 - Implement Repeating-Key XOR](/posts/the-cryptopals-crypto-challenges-set-1-implement-repeating-key-xor)
+ [Hamming Distance Algorithm in C++](/posts/hamming-distance-algorithm-in-c)
+ [The Cryptopals Crypto Challenges: Set 1 - Break Repeating-Key XOR](/posts/the-cryptopals-crypto-challenges-set-1-break-repeating-key-xor)

For this challenge, you are given a [file](http://cryptopals.com/static/challenge-data/7.txt), which contains a ciphertext that has been encrypted using ***AES-128 Cipher*** with ***ECB (Electronic Codebook)*** mode and then encoded using Base64. Decrypt it.

In order to decrypt it, you are given a key:

```text
YELLOW SUBMARINE
```

## What is AES?

[Advanced Encryption Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) a.k.a ***Rjindael***, which was developed by two belgian cryptographers, [Vincent Rijmen](https://en.wikipedia.org/wiki/Vincent_Rijmen) and [Joan Daemen](https://en.wikipedia.org/wiki/Joan_Daemen). ***Rjindael*** is a family of ciphers with various block and key sizes.

***AES-128*** is commonly used but there are also larger key sizes such as ***192*** and ***256*** bits. Similar to ***XOR cipher***, it uses the same key to encrypt and decrypt the message. Till date, there isn't any publication that states if whether ***AES*** is broken but even if you were to break it, it will take atleast a ***billion years*** with a supercomputer, which could beyond the age of the universe.

## What is ECB Mode?

What if your plaintext is longer than (in this case, 128 bits) the keysize? This is where ***ECB*** comes into the picture. [ECB (Electronic Codebook)](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation) is a cipher mode that is used to repeat the key until it covers the entire plaintext (similar to [Repeating-Key XOR Cipher](/posts/the-cryptopals-crypto-challenges-set-1-implement-repeating-key-xor)) and then each ***block*** is independently encrypted using the ***AES*** algorithm to produce the desired ciphertext.

This challenge is not that hard, in fact, it's completely trivial and more like an introduction of ***AES Cipher***. There are so many ways to solve this problem but I chose to solve this problem using ***OpenSSL*** and other commandline tools such as ***xxd*** (used to print the hexdump of a file) on my UNIX terminal.

Here's the solution:

```bash
openssl enc -aes-128-ecb -d -a -in secret.txt -K $(echo "YELLOW SUBMARINE" | xxd -p) -iv 1 | head
```

This is the decrypted message:

```text
I'm back and I'm ringin' the bell
A rockin' on the mike while the fly girls yell
In ecstasy in the back of me
Well that's my DJ Deshay cuttin' all them Z's
Hittin' hard and the girlies goin' crazy
Vanilla's on the mike, man I'm not lazy.

I'm lettin' my drug kick in
It controls my mouth and I begin
To just let it flow, let my concepts go
```

Initially, I was planning to write an implementation of ***AES*** for fun, but then I decided to make it a side project that I can work on as there are a lot of things about ***AES*** that I'd like to talk about in the future.

Stay tuned for the next challenge!