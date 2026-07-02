title: Using Laravel events and listeners in your application
date: February 7th, 2020
slug: using-laravel-events-and-listeners-in-your-application
category: Programming
summary: Sharing my experiences of using events and listeners in my Laravel application.

Recently, I have started learning Laravel and now, I'm building an application for my new company using this amazing framework.

My senior developer was curious and thought of having a conversation with me that went like this:

```text
Senior dev: Hmm, can I have a look at your code?

Me: Oh sure, here take a look.

Senior: (Goes through project file structure)

Senior: So, have you ever thought of using events in your application?

Me: Yeah, I wrote a custom JavaScript file to handle and fire events on the client-side like validating the forms and passing async requests to the server.

Senior: Hmm, that's okay but I'm talking using events in Laravel.
```

At this point, I was pretty clueless and I didn't know what the heck was going on. Events in PHP? I mean, I know about it in JavaScript because of it's event-driven architecture that we are all familiar with. But in PHP? I didn't know that.

Still confused, he proceeds to explain about it's concepts in an abstract manner and thanks to him, it induced my curiosity by asking myself: ***What's the deal in between using events over function calls using a route on a standard controller?***

In today's article, I'll be talking about why and when to use events over function calls using Laravel in your application.

## What's an event?
An event is a piece of reusable logic stored somewhere in your application that has a set of listeners waiting to be executed, if triggered.

Let's say, you have a simple CRUD application that involves user registration. Whenever a user registers, you may want to perform certain actions, such as:

- Adding them into your mailing list
- Confirmation of account

You can add more but this is just to give you an idea. Let's see take a look at two different approaches:

1. [Functional](#approach-1)
2. [Events and Listeners](#approach-2)

### <a id="approach-1"></a> Functional
If you're using an MVC framework (Laravel, in our case), you'd do this in a controller with a bunch of methods like so:

```php
<?php
namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use App\User;

class UserController extends Controller {
    public function index() {
        // insert code to view users page
    }

    public function create(Request $request) {
        $arr = [
            'username' => $request->username,
            'email' => $request->email,
            'password' => bcrypt('something')
        ];

        $user = User::create($arr);

        $this->sendConfirmationEmail($user);
        $this->subscribeToMailingList($user);
    }

    // Send confirmation email to user
    private function sendConfirmationEmail($user) {
        // insert code
    }

    // Subscribe user to mailing list
    private function subscribeToMailingList($user) {
        // insert code
    }
}
?>
```

This is approach is self-contained and simple to follow but you're also adding in a lot of responsibility to your controller.

Not only that, what if the user wants to register from another place in your application, in that case, you'll have to duplicate your logic in multiple places.

### <a id="approach-2"></a> Events and Listeners
Using this approach, you can split this into <mark>Event</mark> and <mark>Listener</mark> files in your application.

```php
<?php
namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use App\User;

class UserController extends Controller {
    public function index() {
        // insert code to view users page
    }

    public function create(Request $request) {
        $arr = [
            'username' => $request->username,
            'email' => $request->email,
            'password' => bcrypt('something')
        ];

        $user = User::create($arr);

        // Emit event
        event(new UserRegistered($user));
    }
}
?>
```

This is how your <mark>UserRegistered</mark> event would look like:

```php
<?php
namespace App\Events;

use Illuminate\Queue\SerializeModels;
use App\User;

class UserRegistered {
    use SerializesModels;

    public $user;

    public function __construct(User $user) {
        $this->user = $user;
    }
}
?>
```

And this is how your <mark>SendConfirmationEmail</mark> listener would look like:

```php
<?php
namespace App\Listeners;

use App\Events\UserRegistered;

class SendConfirmationEmail {

    public function __construct(User $user) {
        // insert code
    }

    public function handle(UserRegister $event) {
        // insert code
    }
}
?>
```

Using this approach, you can use the <mark>UserRegistered</mark> event anywhere you wanted in your application. No matter what happens, it will trigger the same actions as it was intended to do so. If you want to add a new functionality, create a new listener and register it with the event in your <mark>EventServiceProvider</mark> file like this:

```php
<?php
protected $listen = [
    'App\Events\UserRegistered' => [
    'App\Listeners\SendConfirmationEmail',
    ],
];
?>
```

If you follow this approach, your logic complexity is toned down and the controller will have less responsibility.

## Why use events and listeners over function calls?
Just like this answer that I found on [StackOverflow](https://stackoverflow.com/questions/4503723/why-use-event-listeners-over-function-calls) question regarding events and listeners over calling functions:

>You might not be in control of the code that's doing the calling. Or even if you are, you don't want to introduce dependencies into that code.

Think about it, what if you built an API or library that you want people to use but don't want them to modify the source code. Instead, you could provide a documentation that states specific events are raised under specific circumstances, in turn, they can write code that responds to such events.

I'm sure that there are more examples as to where this methodology might be applied.

## When to use it?
Truth be told, it depends. If you have a simple application, then a functional approach is all you need but it's a larger and more complicated application, using Events and Listeners can be a better option.

## Conclusion
Please note, I'm not an expert at this topic as I'm still learning and I thought of sharing what I had learnt. If you have any suggestions or thoughts, please share it with me on [Twitter](https://twitter.com/megacolorboy) or [send me](mailto:megacolorboy@gmail.com) a message to my inbox.

Hope you liked reading this article.

Stay tuned for more.

## Extras

- [Why use event listeners over function calls](https://stackoverflow.com/questions/4503723/why-use-event-listeners-over-function-calls)
- [The meaning of events in PHP](https://stackoverflow.com/questions/17377442/meaning-of-event-in-php)
- [Laravel Events](https://laravel.com/docs/6.x/events)