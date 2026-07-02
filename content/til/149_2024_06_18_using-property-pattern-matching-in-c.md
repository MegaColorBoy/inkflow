title: Using Property Pattern Matching in C#
date: June 17th, 2024
slug: using-property-pattern-matching-in-c
category: C# + Programming
status: active

Alright, we've all been there especially when it comes to writing IF conditions with multiple checks in a single line like the example below:

```csharp
if(employee != null && employee.Age > 20 && employee.Address.City == "Dubai")
{
    // Do something here...
}
```

As you can see, this condition is straight-forward but can sometimes hinder readability and doesn't really ensure type safety.

Here's where you can make use **Property Pattern Matching**.

## What's Property Pattern Matching?

This type of pattern matching is used to match the defined expression if the conditions/nested conditions successfully matches the corresponding property or the field of the result and output of the result is not null. Here's an example of how it might be like:

```csharp
if(employee is { Age: > 20 && Address.City == "Dubai" })
{
    // Do something here...
}
```

This pattern elevates your code's readability, ensures type safety and enable flexibility in terms of data manipulation.

Hope you found this tip useful!