title: Poker Hand Analyser in Python
date: March 30th, 2019
slug: poker-hand-analyser-in-python
category: Algorithms
summary: An algorithm that parses a five-card poker hand and determines it's rank.

<link href="/static/css/playing_cards.css" rel="stylesheet" type="text/css"/>

I've never played Poker and don't think I ever will because I'm not a fan of gambling and placing bets. However, I ran into an interesting problem on [Project Euler](https://projecteuler.net/problem=54) that led me to write a poker hand analyser to determine the rank of each hand.

Before writing this article, I didn't know anything about cards or Poker, I had to do some research on Wikipedia about it. So, forgive me if there's any information that's not accurate in the article.

## Poker Hands
From what I had understood, a ***hand*** is a set of five cards and each card has a rank, which is in the order shown below:

```text
Cards are valued in the order of lowest to highest (Left to Right):
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace
```

Based on the card pattern formed in each hand, the ranking category is determined and it's ranked within it's category based on the ranks of it's cards.

## Hand Ranking Categories

In Poker, there are about 10 ranking categories from lowest to highest:

- [High Card](#highcard)
- [One Pair](#onepair)
- [Two Pairs](#twopairs)
- [Three of a Kind](#threeofakind)
- [Straight](#straight)
- [Flush](#flush)
- [Full House](#fullhouse)
- [Four of a Kind](#fourofakind)
- [Straight Flush](#straightflush)
- [Royal Flush](#royalflush)

Before diving into the code snippets, I wrote a library named [poker_lib.py](https://github.com/megacolorboy/ProjectEuler/blob/master/poker_lib.py) which contains all the methods used in the code snippets.

To make things simple, I created a class named ***Card*** that has two attributes, ***face*** and ***suit***, with ***namedtuple()*** as it's datatype.

### <a id="highcard"></a> High Card

<figure style="text-align: left;">
    <div class="playing_card king_diamonds"></div>
    <div class="playing_card queen_diamonds"></div>
    <div class="playing_card seven_spades"></div>
    <div class="playing_card four_spades"></div>
    <div class="playing_card three_hearts"></div>
</figure>

This hand contains no pairs and it doesn't fall into any other category.

```python
def high_card(hand):
    # collect all faces from each card
    allfaces = [f for f,s in hand]

    #sort the faces and show the highest card
    return "high_card", sorted(allfaces, key=lambda f: allfaces.index(f), reverse=True)[0]
```

### <a id="onepair"></a> One Pair

<figure style="text-align: left;">
    <div class="playing_card ten_spades"></div>
    <div class="playing_card ten_hearts"></div>
    <div class="playing_card eight_spades"></div>
    <div class="playing_card seven_hearts"></div>
    <div class="playing_card four_clubs"></div>
</figure>

This hand contains two cards of one rank and three cards of three other ranks.

```python
def one_pair(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)

    # collect pairs
    pairs = [f for f in allftypes if allfaces.count(f) == 2]

    # if there's more than one pair
    if len(pairs) != 1:
        return False

    allftypes.remove(pairs[0])
    return 'one-pair', pairs + sorted(allftypes, key=lambda f: face.index(f), reverse=True)
```

### <a id="twopairs"></a> Two Pairs

<figure style="text-align: left;">
    <div class="playing_card jack_hearts"></div>
    <div class="playing_card jack_spades"></div>
    <div class="playing_card three_clubs"></div>
    <div class="playing_card three_spades"></div>
    <div class="playing_card two_hearts"></div>
</figure>

This hand contains two cards of one rank, two cards of a second rank and one card of a third rank.

```python
def two_pair(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    
    # collect pairs
    pairs = [f for f in allftypes if allfaces.count(f) == 2]
    
    # if there are more than two pairs
    if len(pairs) != 2:
        return False

    p1, p2 = pairs
    # get the difference using sets
    other_cards = [(allftypes - set(pairs)).pop()]
    return 'two-pair', pairs + other_cards if(face.index(p1) > face.index(p2)) else pairs[::-1] + other_cards
```

### <a id="threeofakind"></a> Three of a Kind

<figure style="text-align: left;">
    <div class="playing_card queen_clubs"></div>
    <div class="playing_card queen_spades"></div>
    <div class="playing_card queen_hearts"></div>
    <div class="playing_card nine_hearts"></div>
    <div class="playing_card two_spades"></div>
</figure>

This hand, also known as trips or a set, contains three cards of one rank and two cards of two other ranks.

```python
def three_of_a_kind(hand):
    allfaces = [f for f,s in hand]

    uniqueRanks = set(allfaces)

    if len(uniqueRanks) != 3:
        return False

    for f in uniqueRanks:
        if allfaces.count(f) == 3:
            uniqueRanks.remove(f)
            return "three-of-a-kind", f

    return False;
```

### <a id="straight"></a> Straight

<figure style="text-align: left;">
    <div class="playing_card ten_diamonds"></div>
    <div class="playing_card nine_spades"></div>
    <div class="playing_card eight_hearts"></div>
    <div class="playing_card seven_diamonds"></div>
    <div class="playing_card six_clubs"></div>
</figure>

This hand contains five cards arranged in a sequential order but not all of them have same suits.

```python
def straight(hand):
    ordered = sorted(hand, key=lambda card: (faces.index(card.face), card.suit))
    if ''.join(card.face for card in ordered) in ''.join(face):
        return 'straight', ordered[-1].face
    return False;
```

### <a id="flush"></a> Flush

<figure style="text-align: left;">
    <div class="playing_card jack_diamonds"></div>
    <div class="playing_card nine_diamonds"></div>
    <div class="playing_card eight_diamonds"></div>
    <div class="playing_card four_diamonds"></div>
    <div class="playing_card three_diamonds"></div>
</figure>

This hand contains five cards of the same suit and not necessarily arranged in sequential order.

```python
def flush(hand):
    allfaces = [f for f,s in hand]

    first_card = hand[0]
    other_cards = hand[1:]

    if all(first_card.suit == card.suit for card in other_cards):
        return 'flush', sorted(allfaces, key=lambda f: face.index(f), reverse=True)

    return False
```

### <a id="fullhouse"></a> Full House

<figure style="text-align: left;">
    <div class="playing_card six_spades"></div>
    <div class="playing_card six_hearts"></div>
    <div class="playing_card six_diamonds"></div>
    <div class="playing_card king_clubs"></div>
    <div class="playing_card king_hearts"></div>
</figure>

This hand, also known as full boat or a boat, contains three cards of one rank and two cards of another rank.

```python
def full_house(hand):
    allfaces = [f for f,s in hand]

    rankFrequency = pe_lib.character_frequency(allfaces)

    # if there are 2 types of ranks and there's a card with 1 pair and 3 of a kind
    if len(rankFrequency) == 2 and (rankFrequency.values()[0] == 2 and rankFrequency.values()[1] == 3):
        return 'full-house'

    return False
```

### <a id="fourofakind"></a> Four of a Kind

<figure style="text-align: left;">
    <div class="playing_card five_clubs"></div>
    <div class="playing_card five_spades"></div>
    <div class="playing_card five_diamonds"></div>
    <div class="playing_card five_hearts"></div>
    <div class="playing_card two_diamonds"></div>
</figure>

This hand, also known as quads, contains four cards of one rank and one card of another rank.

```python
def four_of_a_kind(hand):
    allfaces = [f for f,s in hand]
    
    # create a unique set of ranks
    uniqueRanks = set(allfaces)

    # if there are more than 2 ranks, it's not four of a kind
    if len(uniqueRanks) != 2:
        return False

    for f in uniqueRanks:
        # if there are 4 faces, it is four of a kind
        if allfaces.count(f) == 4:
            uniqueRanks.remove(f)
            return "four-of-a-kind", f

    return False
```

### <a id="straightflush"></a> Straight Flush

<figure style="text-align: left;">
    <div class="playing_card jack_clubs"></div>
    <div class="playing_card ten_clubs"></div>
    <div class="playing_card nine_clubs"></div>
    <div class="playing_card eight_clubs"></div>
    <div class="playing_card seven_clubs"></div>
</figure>

This hand contains five cards arranged in a sequential order with all cards having the same suit.

```python
def straight_flush(hand):
    # sort the cards based on the face rank of each card
    ordered = sorted(hand, key=lambda card: (faces.index(card.face), card.suit))

    first_card = ordered[0]
    other_cards = ordered[1:]

    # check if all are of the same suit
    if all(first_card.suit == card.suit for card in other_cards):
        # check if they are in sequential order
        # compare the ordered faces substring with the face list (which is converted to string)
        if ''.join(card.face for card in ordered) in ''.join(face):
            return 'straight-flush', ordered[-1].face
    return False
```

### <a id="royalflush"></a> Royal Flush

<figure style="text-align: left;">
    <div class="playing_card ten_hearts"></div>
    <div class="playing_card jack_hearts"></div>
    <div class="playing_card queen_hearts"></div>
    <div class="playing_card king_hearts"></div>
    <div class="playing_card ace_hearts"></div>
</figure>

This hand contains the ***royal*** ranks in sequential order in the same suit.

```python
def royal_flush(hand):
    royalface = "TJQKA"
    # sort the cards based on the face rank of each card
    ordered = sorted(hand, key=lambda card: (faces.index(card.face), card.suit))

    first_card = ordered[0]
    other_cards = ordered[1:]

    # check if all are of the same suit
    if all(first_card.suit == card.suit for card in other_cards):
        # check if they are in sequential order
        # compare the ordered faces substring with the face list (which is converted to string)
        if ''.join(card.face for card in ordered) in royalface:
            return 'royal-flush', ordered[-1].face
    return False
```

## Conclusion
It was a fun project to work on and I learnt new styles of array and string manipulation techniques using Python.

Inspired by this, I'm planning to create an interactive version of this project using Javascript and talk about it on another article.

The code for this program can be found in my [GitHub repository](https://github.com/MegaColorBoy/ProjectEuler).

Hope you liked reading this article!

Stay tuned for more!