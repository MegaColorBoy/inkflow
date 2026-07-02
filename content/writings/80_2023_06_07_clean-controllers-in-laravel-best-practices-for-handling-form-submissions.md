title: Clean Controllers in Laravel: Best practices for handling form submissions
date: June 7th, 2023
slug: clean-controllers-in-laravel-best-practices-for-handling-form-submissions
category: Laravel + PHP + Clean Code
summary: Learn how to write clean Laravel controllers for efficient contact form handling using validation, Eloquent, Mail, and events.
status: active

Unlike most frameworks, Laravel is an unopinionated framework and doesn't force the developer to follow a particular pattern.

In this article, I'm going to show you how your codebase could benefit by following Laravel's best practices like separation of concerns, utilizing Laravel's in-built features like Eloquent models, Form Requests and Mail.

To begin with, here's a dirty method that handles a simple contact form submission:

```php
<?php
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Mail;

class ContactController extends Controller
{
    public function submit(Request $request)
    {
        // Validate the form inputs
        $request->validate([
            'name' => 'required',
            'email' => 'required|email',
            'message' => 'required',
        ]);

        // Get the form data
        $name = $request->input('name');
        $email = $request->input('email');
        $message = $request->input('message');

        // Save the form data in the database
        DB::table('contact_forms')->insert([
            'name' => $name,
            'email' => $email,
            'message' => $message,
        ]);

        // Send an email to the user
        $mailData = [
            'name' => $name,
            'email' => $email,
            'message' => $message,
        ];

        Mail::send('emails.contact', $mailData, function ($message) use ($email) {
            $message->to($email)->subject('Thank you for contacting us');
        });

        // Return a response to the user
        return redirect()->back()->with('success', 'Thank you for contacting us! We will get back to you soon.');
    }
}
```

To most developers, this method might seem straight-forward and they might even debate with you that it's completely fine. But allow me to highlight the issues of that this method brings to the table:

1. **Lack of separation of concerns**: The controller is responsible for handling form validation, saving data to the database, and sending an email. This violates the Single Responsibility Principle.

2. **Direct usage of the database query builder**: Instead of utilizing Eloquent models for database interactions, the example directly uses the query builder, which can make the code less maintainable and harder to read.

3. **Inline email sending**: The email sending functionality is implemented inline within the controller method, making the code harder to test and reuse.

4. **Lack of error handling**: The example does not handle any potential errors that may occur during form validation, database insertion, or email sending.

Now, it's time to make it cleaner.

## Save data using Form Requests and Laravel's Eloquent ORM

Let's start with creating a form request that is dedicated to handling the validation logic:

1. Quickly, open up your terminal and type the following command:

```bash
php artisan make:request ContactFormRequest
```

This command will generate a new file named `ContactFormRequest.php` in the `app/Http/Requests` directory.

2. Open the `ContactFormRequest.php` file and modify it as follows:
```php
<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class ContactFormRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     *
     * @return bool
     */
    public function authorize()
    {
        // Set the authorization logic based on your requirements
        // For example, you may check if the user is authenticated or has certain permissions.
        // Return true if the user is authorized to submit the form; otherwise, return false.
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array
     */
    public function rules()
    {
        return [
            'name' => 'required',
            'email' => 'required|email',
            'message' => 'required',
        ];
    }

    public function messages()
    {
        return [
            'name.required' => 'Please enter your name',
            'email.required' => 'Please enter your email address',
            'email.email' => 'Please enter a valid email address',
            'message.required' => 'Write a message before submit the form',
        ];
    }
}
```

In the `rules()` method, you can define validation rules for each field in the form. You can adjust according to your own preferences and if you want to know more about them, [read this documentation](https://laravel.com/docs/10.x/validation).

4. Save the `ContactFormRequest.php` file.

Great, now you have a separate class for validating your contact form and this promotes code-reusability, improves code readability and separates the validation logic from your controller.

Now let's update the `submit()` method in the `ContactController.php` example:

```php
<?php
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Mail;
use App\Http\Requests\ContactFormRequest;
use App\Models\ContactFormModel;

class ContactController extends Controller
{
    public function submit(ContactFormRequest $request)
    {
        // Validate the form inputs
        // All of the validated form data is accessible via this property.
        $validated = $request->validated();

        // Save the submission
        ContactFormModel::create($validated);

        // Send an email to the user
        $mailData = [
            'name' => $name,
            'email' => $email,
            'message' => $message,
        ];

        Mail::send('emails.contact', $mailData, function ($message) use ($email) {
            $message->to($email)->subject('Thank you for contacting us');
        });

        // Return a response to the user
        return redirect()->back()->with('success', 'Thank you for contacting us! We will get back to you soon.');
    }
}
```

Ensure that you have an appropriate model for your `contact_forms` table like `ContactFormModel.php` and update the following like so:

```php
<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class ContactForm extends Model
{
    protected $table = 'contact_forms';

    // Define any additional model configurations, relationships, or methods.
    protected $fillable = [
        'name',
        'email',
        'message'
    ];

    protected $timestamps = true;
}
```

This allows you to leverage Laravel's ORM in which you could benefit from easy quering, relationship management and automatic timestamps.

## Making use of Laravel Events and Mail

1. Generate a new event class by writing the following artisan command:

```bash
php artisan make:event ContactFormSubmitted
```

This will generate a `ContactFormSubmitted` class in the `app/Events` directory.

2. Open up `ContactFormSubmitted.php` file and update as follows:

```php
<?php
namespace App\Events;

use App\Models\ContactForm;
use Illuminate\Foundation\Events\Dispatchable;

class ContactFormSubmitted
{
    use Dispatchable;

    public $contactForm;

    /**
     * Create a new event instance.
     *
     * @param  ContactForm  $contactForm
     * @return void
     */
    public function __construct(ContactForm $contactForm)
    {
        $this->contactForm = $contactForm;
    }
}
```

3. Next, let's generate an event listener using artisan command:
```bash
php artisan make:listener SendContactFormEmail --event=ContactFormSubmitted
```

This command will generate `SendContactFormEmail` event listener in the `app/Listeners` directory.

4. Open the `SendContactFormEmail.php` file and update as follows:

```php
<?php
namespace App\Listeners;

use App\Events\ContactFormSubmitted;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Support\Facades\Mail;
use App\Mail\ContactFormSubmitted as ContactFormSubmittedMail;

class SendContactFormEmail implements ShouldQueue
{
    use InteractsWithQueue;

    /**
     * Handle the event.
     *
     * @param  ContactFormSubmitted  $event
     * @return void
     */
    public function handle(ContactFormSubmitted $event)
    {
        $contactForm = $event->contactForm;

        // Send an email to the user
        Mail::to($contactForm->email)
            ->send(new ContactFormSubmittedMail($contactForm));
    }
}
```

5. Create a mailable class using the following artisan command:

```bash
php artisan make:mail ContactFormSubmitted
```

This command will generate a new `ContactFormSubmitted` mailable class in the `app/Mail` directory.

Now, update the `ContactFormSubmitted.php` file as follows:

```php
<?php
namespace App\Mail;

use App\Models\ContactForm;
use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Mail\Mailable;
use Illuminate\Queue\SerializesModels;

class ContactFormSubmitted extends Mailable implements ShouldQueue
{
    use Queueable, SerializesModels;

    public $contactForm;

    /**
     * Create a new message instance.
     *
     * @param  ContactForm  $contactForm
     * @return void
     */
    public function __construct(ContactForm $contactForm)
    {
        $this->contactForm = $contactForm;
    }

    /**
     * Build the message.
     *
     * @return $this
     */
    public function build()
    {
        return $this->subject('Thank you for contacting us')
            ->view('emails.contact')
            ->with('contactForm', $this->contactForm);
    }
}
```

6. Let's open up the `ContactController.php` and import the necessary classes on top:

```php
<?php
use App\Events\ContactFormSubmitted;
use Illuminate\Support\Facades\Mail;
```

7. Lastly, update the `submit()` method as follows:

```php
<?php
use App\Http\Requests\ContactFormRequest;
use App\Models\ContactForm;
use App\Events\ContactFormSubmitted;
use Illuminate\Support\Facades\Mail;
use App\Mail\ContactFormSubmitted;

class ContactController extends Controller
{
    public function submit(ContactFormRequest $request)
    {
        // Validated form data is accessible via the $validatedData property of the form request instance
        $validatedData = $request->validated();

        // Save the form data in the database using Eloquent
        $contactForm = new ContactForm();
        $contactForm->name = $validatedData['name'];
        $contactForm->email = $validatedData['email'];
        $contactForm->message = $validatedData['message'];
        $contactForm->save();

        // Dispatch an event to handle email sending asynchronously
        event(new ContactFormSubmitted($contactForm));

        // Return a response to the user
        return redirect()->back()->with('success', 'Thank you for contacting us! We will get back to you soon.');
    }
}
```

Ah! Finally, this looks much better now, doesn't it?

By making use of Laravel's Mail method, events and listeners, we've separated the logic for sending emails from the controller. The email is now sent asynchronously using an event and listener combination. This approach improves code organization, maintainability, and scalability.

Hope you found this article to be useful.