title: Using the null-coaleascing operator in C#
date: May 25th, 2024
slug: using-the-nullcoaleascing-operator-in-c
category: C# + Programming
status: active

Null checks are the most underrated thing and despite years of experience, we still forget to write a null check in our code.

When it comes to writing null checks, this is what one would most write:

```csharp
string foo = null;
string bar;
if(foo != null)
{
    bar = foo;
}
else
{
    bar = "Hello, friend!";
}
Console.WriteLine(bar) // Output: Hello, friend!
```

Yes, it does the job but it's a bit lengthy and not so readable. Let's see how the `??` operator i.e. the null-coalescing operator can help simplify your logic:

```csharp
string foo = null;
string bar = foo ?? "Hello, friend!";
Console.WriteLine(bar) // Output: Hello, friend!
```

Now, you can bid goodbyes to writing verbose null checks and make your code more cleaner and readable.

Hope this tip helps you out!