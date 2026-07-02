title: Artificial Intelligence: A Modern Approach - Chapter 1
date: September 1st, 2018
slug: artificial-intelligence-a-modern-approach--chapter-1
category: Artificial Intelligence
summary: An introduction into the foundations of Artificial Intelligence.

It's something that I had in my mind for a long time but never got the
time to execute it but finally, I decided to get out of my comfort zone
to learn new concepts and techniques that would enable me to solve new
problems. Hence, I chose to study ***Artificial Intelligence***.

<figure>
    <img src="http://www-fp.pearsonhighered.com/assets/hip/images/bigcovers/0132071487.jpg"/>
    <figcaption>
        Artificial Intelligence, A Modern Approach (3rd Edition)
    </figcaption>
</figure>

I did some online research and found out a really good book named
[Artificial Intelligence, A Modern Approach (3rd
Edition)](https://www.amazon.com/Artificial-Intelligence-Modern-Approach-3rd/dp/0136042597) by
the [Stuart Russell](https://en.wikipedia.org/wiki/Stuart_J._Russell)
and one of my favorite computer scientists, [Peter
Norvig](https://en.wikipedia.org/wiki/Peter_Norvig) (Director of
Research at Google) to learn about it's concepts and techniques. The
book has 1000+ pages and it's a book used for undergraduate and graduate
level courses in university.

My current knowledge of Artificial Intelligence is pretty basic (e.g:
write game AI) and I want to learn more about it and be able absorb any
information related to it and build toy AI projects.

I've completed the first chapter of the book, so let's dive in because
this going to be a long read.

## What is Artificial Intelligence?

We read about it in the news, it's being deployed in our mobile
applications that we use everyday such as Facebook, Instagram, Twitter,
Reddit and so on to filter out graphic content, fake information and
insensitive political content. It's also being used in games such as
chess, scientific research, diagnosis of several diseases and
self-driving cars.

But do we know what is it? According to Google Search, it means:

> The theory and development of computer systems able to perform tasks
> normally requiring human intelligence such as visual perception,
> speech recognition, decision-making and translation between
> languages. 

It encompasses a huge number of fields and sub-fields and AI is already
the next big thing that it's shaping our everyday life.

## Approaches towards AI

The book states that there are four types of approaches when it comes to
creating an AI:

<figure>
    <img src="https://cs.shaunlgs.com/wp-content/uploads/2017/02/slide_3.jpg"/>
    <figcaption>
        Four approaches towards AI.
    </figcaption>
</figure>

### Acting Humanly

Proposed by British computer scientist [Alan
Turing](https://en.wikipedia.org/wiki/Alan_Turing), the [Turing
Test](https://en.wikipedia.org/wiki/Turing_test) approach was designed
to provide a functional definition of Artificial Intelligence. The test
is proved positive only when a human is unable to tell the difference
between the results of a computer or a human. In order to think like a
human, it should possess the following capabilities:

+ ***Natural Language Processing*** to enable communication in any
    language with the human
+ ***Knowledge Representation*** to store what it knows or hears
+ ***Automated Reasoning*** to make conclusions based on the repository
    of information to answer questions
+ ***Machine Learning*** to learn and adapt to new patterns and
    extrapolations

It is to be noted that the test deliberately avoided interaction with
the human because physical interaction with the human wasn't necessary
for intelligence.

Then came another test called ***Total Turing Test***, this was made to
test the computer's ability of visual perception. The computer passes
this test when it's possess the following abilities:

+ ***Computer Vision*** to be able to perceive and identify objects
+ ***Robotics*** to be able to manipulate physical objects

<figure>
    <img src="https://www.sony.net/SonyInfo/CorporateInfo/newbusiness/AI_Robotics/img/image_movie_sp.jpg"/>
    <figcaption>
        Sony's AIBO Home Entertainment robot.
    </figcaption>
</figure>

The abilities mentioned above, composes most of what modern AI is today
and Turing deserves a huge credit for designing this test that still
remains relevant for more than 60+ years.

### Thinking Humanly

Do we know how humans think? Maybe, but for us to be able to determine
that, we would need to achieve a deep understanding of the human mind
works. There are a few ways such as:

+ ***Introspection*** by catching our own thoughts as they pass by
+ ***Psychological experiments*** by observing the actions or behavior
    of a human
+ ***Brain imaging*** by observing the brain in action

<figure>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Cognitive_Science_Hexagon.svg/800px-Cognitive_Science_Hexagon.svg.png"/>
    <figcaption>
        Fields that contributed to the birth of cognitive science.
    </figcaption>
</figure>

Once we have sufficient information, it's possible to theorize that a
computer program behaves like a human. [Cognitive
Science](https://en.wikipedia.org/wiki/Cognitive_science) enables you to
combine both computational models of an AI and psychological
experimentation techniques to provide testable theories as to how the
human mind works.

### Thinking Rationally

Greek Philosopher [Aristotle](https://en.wikipedia.org/wiki/Aristotle)
attempted to arrange information based on irrefutable evidence based on
the process of reasoning. His rules of inference a.k.a ***syllogisms*** (a
form of reasoning in which conclusions are drawn from various
propositions or a set of premises) provided patterns that yielded
correct conclusions from correct premises. For example: *"Socrates is a
man; All men are mortal; therefore, Socrates is a mortal being"*. These
laws of thought initiated the study of logic, which gave hope to 19th
century logicians to help create intelligent systems.

<figure>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Aristotle_Altemps_Inv8575.jpg/448px-Aristotle_Altemps_Inv8575.jpg"/>
    <figcaption>
        Marble bust of Greek Philosopher Aristotle.
    </figcaption>
</figure>

However, there are two main obstacles to this logical approach. Firstly,
it's difficult to convert informal information into formal terms
required by logical notations especially when the information isn't 100%
certain. Secondly, being able to solve a problem in theory vs. solving a
problem in practice are two different things. You can have a computer
that can solve a problem with a few hundred facts yet use up all of it's
resources.

### Acting Rationally

This is focused on creating ***intelligent agents*** that can perform
various tasks like being able to operate autonomously, perceive objects,
adapt to change, create new goals and pursue them. A ***rational
agent*** is an agent that acts to achieve the best expected outcome.

Making the right conclusions based on evidences i.e. ***correct
inferences*** is part of a rational agent because to act rationally, an
agent must be able to reason with logic to reach to a conclusion for a
given action to achieve one's goals.

However, it doesn't necessarily that it's always "correct", sometimes,
it has there's no such thing as the "right" thing to do but something
must be done.

<figure>
    <img src="https://upload.wikimedia.org/wikipedia/commons/3/3f/IntelligentAgent-SimpleReflex.png"/>
    <figcaption>
        A simple agent reflex.
    </figcaption>
</figure>

The skills needed for a Turing Test allows an agent to act rationally
especially on making good decisions using ***Knowledge
Representation*** and ***Automated Reasoning***, generating intelligible
sentences using ***Natural Language Processing*** for a complex society,
adapting to change and generating effective behavior using ***Machine
Learning***.

But, there are some advantages to this approach. Firstly, it's more
general in terms of the logical approach (mentioned in ***Thinking
Rationally***). Secondly, it's more open to scientific development
compared to human behavior (mentioned in ***Acting Humanly***) and human
thought (mentioned in ***Thinking Humanly***). The standard rationality of
an agent is purely mathematically defined and completely general whereas
human behavior adapts to a specific environment.

Later, the book states that it's focus is going to be based on the
general principles of rational agents and on components for constructing
them.

## Is AI a science, or is it engineering?

As I was reading the book, it was fascinating to see how various
disciplines have contributed ideas, techniques and viewpoints to the
field of Artificial Intelligence. The following disciplines are:

+ Philosophy
+ Neuroscience
+ Mathematics
+ Economics
+ Linguistics
+ Psychology
+ Computer engineering
+ Control theory and cybernetics

Each disciplines had thoughtful questions like How does a human brain
work? How are valid conclusions drawn from formal rules? How can we
build an efficient computer? How to think and communicate in one's
language? How does the brain process large amounts of information? How
do humans and other living things think and act? How does language
relate to thought?

This part of the book is really long but it was a good way to understand
about it's early foundations.

## How is it useful today?

Well, that's not very easy to answer because it's being used in multiple
fields and sub-fields. There are so many applications such as:

+ Self Driving Cars
+ Speech Recognition
+ Facial Recognition
+ Fighting Malware and Spam bots
+ Filtering graphic content and fake information from social media
+ Game playing AIs for different board games like Checkers, Go and Chess

<figure>
    <img src="https://cdn1.i-scmp.com/sites/default/files/styles/980x551/public/images/methode/2018/04/25/2e2a124c-3b92-11e8-b6d9-57447a4b43e5_image_hires_135128.JPG?itok=uWX9_NQ4"/>
    <figcaption>
        Chinese Government surveillance system using Facial Recognition.
    </figcaption>
</figure>

All of this used to be science fiction but thanks to the advancements of
Mathematics, Science and Engineering, it's become a reality in today's
era.

## Conclusion

Well, I don't know if this is one of the longest articles I have ever
written but I really did enjoy writing this because this made me read
the chapter again and gained a better understanding of the concepts.

I will be writing more articles about it, write algorithms and build
toy  implementations of Artificial Intelligence applications.

In fact, I wrote this article to answer all, if not, most of the
questions from the exercises section of this chapter.

Hope you liked reading this article!

Stay tuned for more!

## Extras

+ [Computing Machinery and Intelligence by Alan Turing](https://www.csee.umbc.edu/courses/471/papers/turing.pdf)


