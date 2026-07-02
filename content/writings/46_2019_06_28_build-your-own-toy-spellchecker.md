title: Build your own toy spellchecker
date: July 19th, 2019
slug: build-your-own-toy-spellchecker
category: Algorithms
summary: Wrote a simple toy spellchecker using C++ by taking inspiration from Peter Norvig's article.

Spellcheckers and autocorrect, aren't they magical? They do feel like magic to me. I mean, how is it able to predict what word do you want to type?

According to [Norvig](https://norvig.com), some of the most talented engineers at Google don't have a complete understanding of how a spellchecker works.

Peter Norvig's [solution in Python](https://norvig.com/spell-correct.html) is so elegant and simple, I don't think anyone can write better than that. However, I wanted to know how it works, so I thought of building it to understand it's functionality. Also, an excuse to exercise my C++ skills.

So, are you as curious as I am? If you are, I think you're in the right spot.

## How it works?
Okay, so think about it? What does a spellchecker do? You type in a misspelled word and it returns a word with the highest probability, right? 

Well, there's a little bit more to it.

### Create a word dictionary

First, we must create a dictionary, in order to do that, you need to extract words from a large piece of text and store it in a Hashmap in which each word will have a word count. In this example, I've used a Sherlock Holmes novel (which is around 6MB). The words are extracted from a novel instead of an actual dictionary because it can be used to create a simple Language Model.

**Source code to create a dictionary:**
```cpp
void SpellChecker::extractWords(string &filename)
{
    ifstream infile;
    infile.open(filename);
    string x;
    while(infile &gt;&gt; x)
    {
        x = filterAlpha(x);
        dictionary[x]++;
    }
}

string SpellChecker::filterAlpha(string &word)
{
    for(int i=0; i&lt;word.size(); i++)
    {
        char ch = word[i];

        if(ch &lt; 0)
        {
            word[i] = '-';
        }

        if(isalpha(ch))
        {
            word[i] = tolower(ch);
        }
    }
    return word;
}
```

### Create a list of candidates

Second, we must able to predict/hypothesize the ways of editing text when the user types. It could be one of the following types of editing:

- [Adding a letter](#inserts)
- [Replacing a letter](#replaces)
- [Switching two adjacent letters](#transposes)
- [Removing a letter](#deletes)

Based on the types of edits a user could make, we can generate a list of possible candidates by creating permutations using these edit methods mentioned above.

#### <a id="inserts"></a> Adding a letter

In this method, you generate a list of candidates by inserting a letter in every iteration.

```cpp
void SpellChecker::inserts(string &word, Vector &result)
{
    for(int i=0; i&lt;word.size()+1; i++)
    {
        for(int j=0; j&lt;alphabets.size(); j++)
        {
            char ch = alphabets[j];
            result.push_back(word.substr(0,i) + ch + word.substr(i));
        }
    }
}
```

#### <a id="replaces"></a> Replacing a letter

In this method, you generate a list of candidates by replacing each character with a letter from a list of alphabets in every iteration.

```cpp
void SpellChecker::replaces(string &word, Vector &result)
{
    for(int i=0; i&lt;word.size(); i++)
    {
        for(int j=0; j&lt;alphabets.size(); j++)
        {
            char ch = alphabets[j];
            result.push_back(word.substr(0,i) + ch + word.substr(i+1));
        }
    }
}
```

#### <a id="transposes"></a> Switching two adjacent letters

In this method, you generate a list of candidates by switcing two adjacent letters in every iteration. For example: the word "ornage" would look like this: "orange", when the letters "n" and "a" are swapped.

```cpp
void SpellChecker::transposes(string &word, Vector &result)
{
    for(int i=0; i&lt;word.size()-1; i++)
    {
        result.push_back(word.substr(0,i) + word[i+1] + word[i] + word.substr(i+2));
    }
}
```

#### <a id="deletes"></a> Removing a letter

In this method, you generate a list of candidates by removing a letter in every iteration.

```cpp
void SpellChecker::deletes(string &word, Vector &result)
{
    for(int i=0; i&lt;word.size(); i++)
    {
        result.push_back(word.substr(0,i) + word.substr(i+1));
    }
}
```

All of these methods are called in one wrapper method:
```cpp
void SpellChecker::edits(string &word, Vector &result)
{
    //Deletion
    deletes(word, result);

    //Transposition
    transposes(word, result);

    //Replacement
    replaces(word, result);

    //Insertion
    inserts(word, result);
}
```

### Extract the known words

Third, at this stage, the above step would've generated a huge list of words but 90% of them would be gibberish, so we need to "clean" the list and extract the known words using the dictionary we've created.

```cpp
void SpellChecker::known_words(Vector& results, Dictionary &candidates)
{
    Dictionary::iterator end = dictionary.end();

    for(int i=0; i&lt;results.size(); i++)
    {
        Dictionary::iterator val = dictionary.find(results[i]);

        if(val != end)
        {
            candidates[val->first] = val->second;
        }
    }
}
```

The <mark>edits()</mark> method apply to words that have a edit distance of 1, what if it was 2 or more? Like if the user typed "the", it could've been "then" or "they". So, all you have to do is create a method that generates a new set of permutations based on the already generated list of edited words and extract the known words.

```cpp
void SpellChecker::edits2(Vector &result, Dictionary &candidates)
{
    for(int i=0; i&lt;result.size(); i++)
    {
        Vector edit2;

        edits(result[i], edit2);
        known_words(edit2, candidates);
    }   
}
```

### Display the correct word

In order to determine the correct word, the following possibilities are considered:

1. Check if this word is in the dictionary, if it does, display it.
2. Generate known words that have an edit distance of 1 and check in the dictionary, if it does, display it.
3. Generate known words that have an edit distance of 2 and check in the dictionary, if it does, display it.
4. If all else fails, this word is unique or not a known word.

<p></p>

```cpp
string SpellChecker::correct(string &word)
{
    Vector result;
    Dictionary candidates;

    string file = "big.txt";

    //1. if it's in the dictionary, display it
    if(dictionary.find(word) != dictionary.end())
    {
        return word;
    }

    extractWords(file);

    edits(word, result);
    known_words(result, candidates);

    //2. if it's a known word but one edit away
    if(candidates.size() &gt; 0)
    {
        return max_element(candidates.begin(), candidates.end())-&gt;first;
    }

    //3. if it's a known word but two edits away
    edits2(result, candidates);

    if(candidates.size() &gt; 0)
    {
        return max_element(candidates.begin(), candidates.end())-&gt;first;
    }

    //4. Display nothing if it doesn't exist
    return "This word doesn't exist!";
}
```

However, for conditions 2 and 3, the word displayed would most likely have the highest word frequency in the dictionary.

## Conclusion
Phew! I hope that wasn't a long read. Although, I've written this on C++, I plan to rewrite this on Javascript for some of my future projects.

To be honest, I don't think it's completely accurate, although, I got most of the words correct when tested.

The source code can be found on my [GitHub](https://www.github.com/megacolorboy/ToySpellChecker) repository.

Hope you liked reading this article!

Stay tuned for more!