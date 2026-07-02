title: Can we eliminate traffic congestion with the help of Computer Vision?
date: August 19th, 2018
slug: can-we-eliminate-traffic-congestion-with-the-help-of-computer-vision
category: Essay
summary: Writing out my thoughts on eradicating traffic congestion in highly populated cities.

Whether it's being implemented or not, I have been thinking on how we
could use ***Computer Vision*** to solve traffic congestion.

Since, I live in the ***United Arab Emirates***, I have always observed
that people who commute from ***Sharjah*** to ***Dubai*** and vice-versa
face a lot of traffic jams despite all the new roads and toll-gates
(yes, I don't seem to understand how does that solve the problem).

<figure>
    <img src="https://images.khaleejtimes.com/storyimage/KT/20160203/ARTICLE/302039854/AR/0/AR-302039854.jpg&MaxW=780&imageVersion=16by9&NCS_modified=20160203204300"/>
    <figcaption>
        Traffic in Al Ittihad Highway.
    </figcaption>
</figure>

Well, the problem is not only faced in this country but many countries
such as China, Indonesia and so on.

## What are the causes of traffic congestion?

Anyways, I jotted down some facts to consider what causes traffic
congestion in the first place:

+ Tail-gating
+ Inconsistent travel speeds
+ Uneven vehicular distances
+ Spontaneous accidents and road rages
+ Changing from one lane to another
+ Increase in car population
+ Peak hours i.e. people going to work and leaving from work

I'm sure that there could be more but these are the facts that I can
come up with for now.

## How can Computer Vision solve this problem?

[Computer Vision](https://en.wikipedia.org/wiki/Computer_vision) is a
field that intersects with multiple areas of technologies in which it
aims to develop an understanding of objects by extracting information
from various digital media sources like images and videos and automate
those tasks that a normal human would do in their daily lives.

<figure>
    <img src="https://www.onlinebooksreview.com/uploads/blog_images/2018/04/16_computer_vision.jpg"/>
    <figcaption>
        Visualization of Computer Vision.
    </figcaption>
</figure>

There are various types of problems that Computer Vision algorithms are
able to solve but not limited to:

+ Object Recognition or Object Classification
+ Identification of Objects
+ Object Detection
+ Analysis of Motion

Now, it's not only about implementing these ***CNN***-based
([Convolutional Neural
Network](https://en.wikipedia.org/wiki/Convolutional_neural_network))
algorithms but you also need hardware to be able to compute and process
data. 

## How would this work?

There are two scenarios that I had thought while writing this article
and I hope that I'm able to translate my thoughts into accurate
examples.

Let's pretend we have four car drivers: Alex, Bob, Charlie and Dylan.

### Speed-Distance equilibrium

Alex, Bob and Charlie are driving on the same lane. Alex hits the brake
slowly to shift to another lane, the sensors of Bob's car detects a
change in speed in Alex's car, Bob's car adjusts it's speed to match
Alex's current speed based on the variables of distance and travel time,
Charlie's car adapts the changes of Bob's car and thus, it's a chain
reaction.

### Shifting from one lane to another

Alex is driving in Lane A and Dylan is driving in Lane B. Alex wants to
shift to Lane B, so he switches on the indicator and Dylan's car sensors
identify that Alex's car wants to change lanes. So Dylan's car slows
down and Alex is able to shift lanes with ease. I thought of it to be
some sort of a ***"elastic"*** effect when this occurs.

Well, you might argue that some cars have a system called ***"Cruise
Control"*** but here's the part that I'm trying to pitch, as I had
mentioned above, I just wanted to integrate sensors to the front and
rear sides of a vehicle, which means that these sensors can be
integrated in almost any vehicle.

## How is this going to be helpful?

For starters, traffic congestion will gradually reduce, if not, be
eliminated but there are other beneficial factors to it, such as:

+ Less fuel consumption
+ Less time is required to reach a destination
+ No tail-gating
+ Could prevent major road accidents

However, if the sensors fail to work, the car driver will still be safe
because it's surrounded by other cars that have the sensors. This made
me think of another question, does that mean do all cars require sensors
or only a few? I find it quite intriguing.

## Conclusion

Although, these sensors might require a vehicle to have some intelligent
capabilities, it may not require the type of network found in an
autonomous vehicle.

<figure>
    <img src="https://i.pinimg.com/originals/b4/7c/00/b47c00d89eb8527be3f47578958f691e.gif"/>
</figure>

The idea of placing sensors in the front and rear of a vehicle can
optimize the flow of traffic and thus, it might help eliminate traffic
congestion.

Hope you liked reading this article!