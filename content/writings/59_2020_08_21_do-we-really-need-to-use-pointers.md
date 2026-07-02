title: Do we really need to use pointers?
date: August 21st, 2020
slug: do-we-really-need-to-use-pointers
category: Programming
summary: Did a little digging on whether it's useful to make use of pointers in your application
status: active

The topic about pointers isn't new as you're probably introduced to this concept in your first computer science class. I started learning Go and once again, I came across the concept of using Pointers and wanted to finally understand, why are they used and do we really need to use it?

Frankly, I don't really remember using pointers when I was developing web applications in PHP and JavaScript but it was quite a refresher to get back on track again.

## Well, what is a pointer?
In it's basic form, a pointer is a variable that contains the memory address of another variable.

For example, you have a variable named <mark>x</mark> that contains some data, in this case, we'll store an integer:

```go
package main

import "fmt"

func main() {
    x := 10
    fmt.Println(x) // prints 10
}
```

The code above prints the variable <mark>x</mark> by referring to it's name. We can do the same using pointers by referring to it's memory address via another variable that points to variable <mark>x</mark>.

To do this, we must use <mark>&</mark> operator to get the address and `*` to return the value stored in the address of variable <mark>x</mark> like this:

```go
package main

import "fmt"

func main() {
    x := 10
    p := &x
    fmt.Println(x)   // prints 10
    fmt.Println(*p)  // also, prints 10
}
```

Hmm, that was pretty straight forward.

## So, why was it created?
In the modern era, most high-level programming languages are capable of handling memory allocation (like **Java** or **C#**), automatically.

But when **C** was developed, computers weren't as powerful as today but that also meant the programmers must create systems that made use of memory and speed, efficiently. Which is why some tasks do require it when programming low-level embedded systems or microcontrollers.

## Why use them?
Whenever you pass a variable to a function, you're basically creating a copy of the variable. But if you're using pointers, you just have to pass the address of the variable and in most cases, a pointer is much smaller in size than the value being pointed at.

It allows you share data and it's quite appropriate when it comes to modifying the data being passed to it.

To some extent, it might seem efficient but there are some tradeoffs, when you're going to talk about optimization.

## Do pointers really optimize your application?
I was thinking if pointers are used to optimize applications, I mean, you don't have to duplicate data and it saves memory, so why not?

Turns out that there are a few points that I came across:

1. Accessing values can use up memory though not so much but it can add up.
2. Data will be placed on top of heap stack which increases the memory overhead and can be cleaned up the garbage collector.

Most programmers tend to avoid using it in order to make their codebase less complex and reduce the increased work for the garbage collector.

Apart from that, there are some concerns when it comes to the security of the application implying that it could be unsafe when using pointers.

## Takeaway
Pointers are useful but don't think of using it, blindly, by assuming that it might give you a boost in performance.

Hope you found this article useful!

## Readings
- [Why C has pointers?](http://duramecho.com/ComputerInformation/WhyCPointers.html)
- [Why do we use pointers in Java but we use them in C and C++](https://www.quora.com/Why-dont-we-use-pointers-in-Java-but-we-use-them-in-C-and-C++)