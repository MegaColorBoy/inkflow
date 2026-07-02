title: Rewriting my SSG again — The right way
date: February 15th, 2026
slug: rewriting-my-ssg-again-the-right-way
category: Refactoring + Personal Challenge + Python
status: active

Around eight years ago, I wrote my own static site generator in Python. It was very simple. No frameworks, no strong structure — just scripts that generated pages for my blog.

It worked, so I kept using it.

There were no proper validations. No structured exception handling. Almost no separation of concerns. I didn’t follow standard practices. At that time, it was just a hobby project, and I only cared that it produced HTML files correctly.

And it did.

To be honest, I was too lazy to rewrite it and it was "stable" enough, so I ignored the technical debt.

## Contrasting differences

Over the years, I’ve worked on much larger and more structured systems — enterprise APIs, background services, integrations, layered architectures. I’ve learned to care about validation, clean boundaries, proper error handling, and maintainability.

Now when I open my old SSG code, I can clearly see the difference.
 
It reflects how I used to think about code.

It’s not terrible. It’s just basic. It lacks discipline.

There’s no validation layer. No clear contracts. Some modules handle too many responsibilities. Dependencies are outdated. Type hints are either missing or inconsistent.

The real issue is that it works — but extending it doesn’t feel comfortable.

## Why I decided to rewrite it?

This rewrite is not about fixing bugs. There are no critical issues. It’s just that single god-like python class is really bugging me.

I want to:

* Add proper validation
* Introduce structured exception handling
* Strengthen type hints
* Upgrade dependencies
* Separate responsibilities clearly
* Make it easier to extend in the future

I also want to refresh my blog properly. If I’m going to continue building on top of this tool, it should be something I trust and feel comfortable maintaining.

Right now, adding a new feature feels like touching something fragile. After refactoring, I want it to feel stable and predictable.

## Time for some justice!

This time, I’m approaching it like a real project, even though it’s still personal.

Clear module boundaries. Explicit data models. Proper validation. Clean CLI entry points. Better organization overall.

I’ll be using PyCharm heavily during this process. When renaming models, reorganizing modules, or tightening type contracts, I want safe refactoring and immediate feedback. Strong inspections and accurate **find usages** will help a lot when reshaping older code.

Tooling becomes more important during refactoring than during initial development.

I’m not trying to over-engineer it. I’m just trying to build it properly — based on what I’ve learned over the years.

## Conclusion

Sometimes old code is not a mistake. It’s just a snapshot of your earlier experience.

Rewriting this SSG is simply updating it to match how I think today.

Over the next few days, I’ll be cleaning it up and rebuilding it with better structure. Not because it failed — but because I’ve improved.

Hope you liked reading this article!