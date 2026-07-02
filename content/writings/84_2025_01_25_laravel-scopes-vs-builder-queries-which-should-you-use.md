title: Laravel Scopes vs. Builder Queries: Which Should You Use?
date: January 25th, 2025
slug: laravel-scopes-vs-builder-queries-which-should-you-use
category: Laravel + PHP
status: active

If you're building a Laravel application, you're probably spending a lot of time writing queries. And as your project grows, you'll inevitably face this question: *Should I use scopes or builder queries?* While both have their place, choosing the right tool for the job can make a world of difference. Here's my opinionated take on the matter.

## The Case for Scopes

**Scopes** are, quite simply, one of Laravel's hidden gems. They let you encapsulate common query logic within your models, making your code clean, reusable, and easy to read. Think of them as tiny, purposeful functions designed to save you time and sanity.

Take this example:

```php
<?php
    // In your model
    public function scopeActive($query)
    {
        return $query->where('status', 'active');
    }

    // Usage
    $activeUsers = User::active()->get();
?>
```

Suddenly, instead of littering your controllers with `where('status', 'active')` everywhere, you have a single, reusable method that reads like English. Scopes shine when you need commonly used filters like `active`, `published`, or `recent`. They’re easy to use, they’re consistent, and they make your code feel more intuitive.

### Why I Prefer Scopes for Reusability

Here’s the thing: in any sizable Laravel app, you’ll inevitably find patterns in your queries. Rewriting the same query logic over and over? That’s a code smell. By using scopes, you centralize your query logic, reducing redundancy and improving maintainability.

For example:

```php
<?php
    $pubishedPosts = Post::published()->recent()->get();
?>
```

This reads beautifully and keeps your codebase DRY (Don’t Repeat Yourself). If the definition of "published" or "recent" changes, you only need to update it in one place. Scopes turn repetitive query logic into single lines of magic.

## The Case for Builder Queries

That said, not everything belongs in a scope. Some queries are just too specific, too complex, or too dynamic. This is where **builder queries** come in.

Imagine you’re building a report that requires multiple joins, conditional logic, or dynamic filters. Scopes could become unwieldy here. Instead, a well-crafted builder query in your controller, service, or repository might make more sense:

```php
<?php
    $users = User::where('status', 'active')
        ->whereDate('created_at', '>', now()->subDays(30))
        ->orderBy('created_at', 'desc')
        ->get();
?>
```

Builder queries are perfect for:

- One-off operations.
- Highly dynamic queries.
- Scenarios where scopes would make your models bloated or overly complex.

The flexibility of builder queries is unmatched. You can construct them on the fly, adapt them to user inputs, and handle edge cases without worrying about making your models an unreadable mess.

## My Opinionated Take: Use Scopes as a Default, Builder Queries for the Edge Cases

If I had to pick a side, I’d say: lean on scopes as your default tool, and reserve builder queries for those rare cases when scopes just don’t cut it. Why?

1. **Scopes enhance readability.** Your queries read like sentences, and your intentions are crystal clear.
2. **Scopes promote DRY principles.** They’re reusable and encapsulate logic, which makes future maintenance a breeze.
3. **Builder queries are powerful but can become messy.** Unless you’re careful, a complex query in your controller can grow into a sprawling monstrosity. Keep your controllers lean and delegate to scopes or dedicated query classes where possible.

## When Not to Use Scopes

There are times when using a scope might do more harm than good:

- **Too much complexity:** If a scope needs multiple parameters or involves complex joins, it’s better suited as a custom query builder or a dedicated repository method.
- **Rarely used logic:** Don’t clutter your models with scopes for queries that are only needed once or twice.
- **Dynamic, user-driven queries:** When filters are highly variable, builder queries give you the flexibility you need.

## Conclusion: Balance Is Key

Laravel gives you powerful tools to write queries, and both scopes and builder queries have their roles. Use scopes to simplify and centralize reusable logic, and reach for builder queries when flexibility and complexity demand it. By balancing both, you’ll keep your codebase clean, maintainable, and a joy to work with.

So, what’s your take? Are you a scope enthusiast or a builder query champion? Either way, Laravel’s got you covered.