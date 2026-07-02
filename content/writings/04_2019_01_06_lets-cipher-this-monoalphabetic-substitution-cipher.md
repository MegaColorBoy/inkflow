title: Let's Cipher This: Monoalphabetic Substitution Cipher
date: May 13th, 2017
slug: lets-cipher-this-monoalphabetic-substitution-cipher
category: Cryptography
summary: An article about monoalphabetic substitution ciphers, it's applications and variations.

<link rel="stylesheet" href="/static/projects/cipher/css/style.css" type="text/css"/>
<script defer type="text/javascript" src="/static/projects/cipher/js/script.js"></script>

This is the first post in the ***"Let's Cipher This!"*** series and in this post, I'll be talking about the various versions of [Monoalphabetic Substitution Ciphers](https://en.wikipedia.org/wiki/Substitution_cipher) such as:

+ [Atbash Cipher](#atbash)
+ [Caesar Cipher](#caesar)
+ [Affine Cipher](#affine)

This post will be a bit longer than my previous ones as I had been occupied with a lot of work and other commitments. But I do feel the need to post something atleast once a month with good content, as it keeps me productive (especially during weekends), so hope you'll find this information useful!

## What's a Monoalphabetic Substitution Cipher?
It's a type of substitution cipher that is used to replace each letter of a plaintext with another letter using a fixed number or replacement structure, which makes up the ciphertext. There are many variations of these, but today, I have decided to talk about a few that I have mentioned, in the beginning.

---

## <a id="atbash"></a> Atbash Cipher
<div id="atbash_cipher_div" class="box"></div>
Atbash Cipher is a monoalphabetic substitution cipher which is used, originally, to encode Hebrew Alphabets but when modified, it can also be used with any alphabets.

### Algorithm
The algorithm is pretty straight-forward, if you have a plaintext of ***"ABCDEFGHIJKLMNOPQRSTUVWXYZ"***, then the ciphertext would be the exact reverse of the plaintext: ***"ZYXWVUTSRQPONMLKJIHGFEDCBA"***.

```text
original: ABCDEFGHIJKLMNOPQRSTUVWXYZ
reversed: ZYXWVUTSRQPONMLKJIHGFEDCBA
```

### Encryption
Encrypting the message is very simple, you just have to replace every letter of the plaintext with the ciphertext, for example, ***'A'*** would become ***'Z'*** and ***'T'*** would become ***'G'*** and the whole message would be encrypted in this manner.

```text
plaintext:  ATTACKONTITAN
ciphertext: ZGGZXPLMGRGZM
```

### Decryption
Decrypting the Atbash Cipher is the opposite of it's encryption process, for example, ***'Z'*** would become ***'A'*** and ***'G'*** would become ***'T'*** and the whole message would be decrypted in this manner.

```text
ciphertext: ZGGZXPLMGRGZM
plaintext:  ATTACKONTITAN
```

### Cryptanalysis
As you might have understood, this is not a secure cipher and in fact, can be broken very easily, assuming, that the ciphertext has been enciphered using Substitution Cipher or by determining the key by trying out each and every letter i.e. using hill-climbing technique.

However, it can be a bit secure if you add some numbers and punctuation to the plaintext alphabets:

```text
original:  .,?!ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
reversed: 9876543210ZYXWVUTSRQPONMLKJIHGFEDCBA!?,.
```

---

## <a id="caesar"></a> Caesar Cipher
<div id="caesar_cipher_div" class="box"></div>
Caesar Cipher is one of the most widely known and simplest substitution ciphers (you probably heard about it or were introduced to it in one of your earlier computer science classes by your ingenious professor!), in which each letter from the plaintext is replaced with another letter that is determined by a fixed number of positions or ***"shifts"***. This is named after [Julius Caesar](https://en.wikipedia.org/wiki/Julius_Caesar), who used it to send private messages that are related to military intelligence with a shift of 3. This is also used in modern [ROT-13](https://en.wikipedia.org/wiki/ROT13) system with a shift of 13.

### Algorithm
The ciphertext is made by aligning two alphabets, so in this case, I will be using a shift of 15 i.e. letter ***'A'*** would be letter ***'P'*** and letter ***'B'*** would be letter ***'Q'*** and so on.

```text
plaintext:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
ciphertext: PQRSTUVWXYZABCDEFGHIJKLMNO
```

### Encryption
The encryption process is represented using [Modular Artihmetic](https://en.wikipedia.org/wiki/Modular_arithmetic) by transforming the letters into it's positions and the mathematical formula is:

```text
E(x) = (x + n) mod 26
```

By using this formula, we can encrypt our plaintext with a shift of 15:

```text
shifts(n): 15

plaintext:               H  E  L  L  O  W  O  R  L  D
integers(x):             7  4  11 11 14 22 14 17 11 3
E(x) = (x + 15) % 26:    22 19 0  0  3  11 3  6  0  18
ciphertext:              W  T  A  A  D  L  D  G  A  S
```

### Decryption
The decryption, again, is done is reverse with a shift of 15 using Modular Arithmetic i.e. letter ***'P'*** would be letter ***'A'*** and letter ***'Q'*** would be letter ***'B'*** and so on. The mathematical formula for deciphering the text is:

```text
D(x) = (x - n) mod 26
```

We can use this formula to decrypt the ciphertext:

```text
shifts(n): 15

ciphertext:              W  T  A  A  D  L  D  G  A  S    
integers(x):             22 19 0  0  3  11 3  6  0  18
D(x) = (x - 15) % 26:    7  4  11 11 14 22 14 17 11 3
plaintext:               H  E  L  L  O  W  O  R  L  D
```

### Cryptanalysis
Caesar Cipher is insecure and can be easily broken in two scenarios:

+ If the cryptanalyst deduces that it's a Caesar Cipher but doesn't know the shift key.
+ If the cryptanalyst figures out that some sort of substitution cipher is used but doesn't know that it's Caesar Cipher.

In the first scenario, it's more straightforward as there are only a limited number of possible shifts (e.g. 26 in English) and can use a [Brute Force](https://en.wikipedia.org/wiki/Brute-force_attack) atack to crack the ciphertext. For the second one, it can be broken using techniques like [Frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis) or looking for patterns.

---

## <a id="affine"></a> Affine Cipher
<div id="affine_cipher_div" class="box"></div>
Affine Cipher is a type of monoalphabetic substitution cipher but it's different compared to Atbash Cipher but similar to Caesar Cipher, where each alphabet is mapped to it's numerical equivalent and then it is encrypted using a simple mathematical function.

### Algorithm
The letters are first mapped to the integers in the range of ***0, 1, ..., m-1(m = the length of the alphabets used)***, which then uses a [Modular Arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic) method to convert the integers to it's corresponding letter.

```text
alphabets: A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
integers:  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
```

### Encryption
The mathematical formula for encrytion is:

```text
E(x) = (ax + b) mod m    
```

In this formula, ***a*** and ***b*** are the keys of the cipher and ***m*** is the size of the alphabet. The key ***a*** must be chosen in such a way that ***a*** and ***m*** are [coprime](https://en.wikipedia.org/wiki/Coprime_integers) i.e. "***a*** should not have any common factors with ***m***."

### Decryption
Unlike the encryption formula, the decryption process of the ciphertext is performed inversely to retrieve the plaintext:

```text
D(x) = c(y - b) mod m
```

In this formula, ***c*** is the [Modular Multiplicative Inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse) of ***a***. In order to find the multiplicative inverse of ***a***, you need to find a number ***x*** in such a way that it satisfies the following equation:

```text
ax = 1 (mod m)    
```

### Explanation
Let's say you want to encrypt a plaintext that says "HELLOWORLD" with ***a = 5*** and ***b = 8***. The reason I chose "5" for ***a*** is because it has to be relatively prime with 26.

```text
plaintext:    H  E  L  L  O  W  O  R  L  D
integers(x):  7  4  11 11 14 22 14 17 11 3
```

Now, you have to take each value of x and convert it to a different letter using the encryption formula mentioned above:

```text
key a = 5
key b = 8

plaintext:               H  E  L  L  O  W  O  R  L  D
integers(x):             7  4  11 11 14 22 14 17 11 3
E(x) = 5(x) + 8 % 26:    17 2  11 11 0  14 0  15 11 23
ciphertext:              R  C  L  L  A  O  A  P  L  X        
```

Okay, let's decrypt the ciphertext that says "RCLLAOAPLX" to "HELLOWORLD" using the same keys ***(a = 5, b = 8)***:

```text
ciphertext:   R  C  L  L  A  O  A  P  L  X    
integers(y):  17 2  11 11 0  14 0  15 11 23       
```

Before we proceed, we need to find the modular inverse of ***a***, in this case, it would be 21. You can find the modular inverse using the [Extended Euclidean](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm) algorithm, which uses [Greatest Common Divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor) ***(GCD)*** of both ***a*** and ***m***. If ***a*** has a modular inverse modulo ***m***, then the GCD must be 1.

Once you find ***a***, we can start decrypting the ciphertext:

```text
key a = 5
key b = 8

ciphertext:              R  C  L  L  A  O  A  P  L  X    
integers(y):             17 2  11 11 0  14 0  15 11 23
D(y) = a(y - 8) % 26:    7  4  11 11 14 22 14 17 11 3
plaintext:               H  E  L  L  O  W  O  R  L  D
```

### Cryptanalysis
Affine Cipher is known to be a very insecure cipher as it's just another version of Caesar Cipher, which is due to it being a monoalphabetic substitution cipher. If a cryptanalyst is able to discover 2 or more common characters using techniques like [Brute Force](https://en.wikipedia.org/wiki/Brute-force_attack), [Frequency Analysis](https://en.wikipedia.org/wiki/Frequency_analysis) or maybe even guessing, the key can then be obtained via solving a [Simultaneous Equation](https://en.wikipedia.org/wiki/Simultaneous_equations), since ***a*** and ***m*** are coprime, it can discard any wrong keys easily in an automated program.

---

## What's next?
So I hope you have understood what's a [monoalphabetic substitution](https://en.wikipedia.org/wiki/Substitution_cipher) cipher and it's applications and variations. You can play around with the encryption tools above or experiment with your own messages to see how it works and prank your friends with it! 

## References
+ [Practical Cryptography: Caesar Cipher](http://practicalcryptography.com/ciphers/caesar-cipher)
+ [Practical Cryptography: Atbash Cipher](http://practicalcryptography.com/ciphers/atbash-cipher-cipher)
+ [Practical Cryptography: Affine Cipher](http://practicalcryptography.com/ciphers/affine-cipher)