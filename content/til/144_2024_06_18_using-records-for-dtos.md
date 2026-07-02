title: Using records for DTOs
date: June 18th, 2024
slug: using-records-for-dtos
category: .NET Core + C# + OOP
status: active

If you're building an application or API using .NET Core in where you might have to integrate with any external services or third-party APIs, this is for you.

## What are records?

It's a feature introduced since **C# 9.0** that allows you to create simple and immutable data types. When representing DTOs (Data Transfer Objects), it comes in handy because the syntax in concise and it's primarily used to transfer data between layers of an application such as the Core and Presentation Layer. 

Here's an example of a car using a regular `class` type:

```csharp
public class Car
{
    public string Manufacturer { get; init; }
    public double Price { get; init; }
    public string Color { get; init; }
}
```

And here's a simplified version of that using `record` type:

```csharp
public record Car(
    string Manufacturer,
    double Price,
    string Color
);
```

Making use of the `record` type to manage Data Transfer Objects makes use of clean coding practicies by writing concise yet maintainable code.

## So, no need of using classes?

Well, it depends because records aren't meant to replace classes for all scenarios. It's still recommended to use regular classes for complex types with complex behavior and whereas, records can be used for simple data structures.

Hope you found this article useful!