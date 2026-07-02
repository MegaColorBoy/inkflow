title: Is SELinux complicated?
date: December 25th, 2021
slug: is-selinux-complicated
category: DevOps
summary: If you turn off SELinux for a living, try this.
status: active

This might look a rant post but hear me out, okay?

Ever deployed an application on CentOS and tried to figure out why it isn't working when it's caused due to some permission issue by SELinux enabled?

Yeah, I know how annoying that is. So, whenever I go on StackOverflow, many people suggest to completely turn it off.

Well, it might be tempting to type `sudo setenforce 0` (which sets SELinux to Permissive mode), I wouldn't really recommend you to edit the SELinux config and disable it completely.

I recently read a blog post on CentOS's official blog and I'd like to quote them for asking this:

> But why do articles feel the need to outright deactivate SELinux rather than help readers work through any problems they might have? Is SELinux that hard?

Good question. Is it really that hard or is it because we don't really understand it? I think it's the latter.

## But why so?

I guess, as users, we really need some sort of user interface to receive feedback because not everyone is really good at the terminal and most importantly, not good at memorizing options and flag combinations.

Here's a sample error that I would face sometimes while deploying a Laravel web application on CentOS 7:

```bash
[Mon May 16 11:39:32.996441 2016] [:error] [pid 2434] [client XXX.XXX.XXX.XXX:8080] PHP Fatal error:  Uncaught UnexpectedValueException: The stream or file "/var/www/html/MYSITE/storage/logs/laravel.log" could not be opened: failed to open stream: Permission denied in /var/www/html/MYSITE/bootstrap/cache/compiled.php:13701
Stack trace:
#0 /var/www/html/MYSITE/bootstrap/cache/compiled.php(13635): Monolog\\Handler\\StreamHandler->write(Array)
#1 /var/www/html/MYSITE/bootstrap/cache/compiled.php(13396): Monolog\\Handler\\AbstractProcessingHandler->handle(Array)
#2 /var/www/html/MYSITE/bootstrap/cache/compiled.php(13494): Monolog\\Logger->addRecord(400, Object(Symfony\\Component\\Debug\\Exception\\FatalErrorException), Array)
#3 /var/www/html/MYSITE/bootstrap/cache/compiled.php(13189): Monolog\\Logger->error(Object(Symfony\\Component\\Debug\\Exception\\FatalErrorException), Array)
#4 /var/www/html/MYSITE/bootstrap/cache/compiled.php(13160): Illuminate\\Log\\Writer->writeLog('error', Object(Symfony\\Component\\Debug\\Exception\\FatalErrorException), Array)
# in /var/www/html/MYSITE/bootstrap/cache/compiled.php on line 13701
```

By looking at this error, you do understand it's permission-related but it doesn't really indicate that it's an SELinux problem because there could be thousands of reasons why there could be such an error. And of course, when I look it up on Google, I do find many people facing the same issue due to SELinux being enabled.

Instead of disabling it completely, I would try doing this:

```bash
chcon -R -t httpd_sys_rw_content_t storage
```

And off goes the error and the application didn't give any permission-related issues again.

Is it worth disabling SELinux? No. 

But does SELinux have an issue of being user friendly? I guess, yes.

I'm just like you, sometimes, I do switch off SELinux at times when it's critical to deploy the application so that I can leave home early but that's not really a good practice.

## Conclusion

I do wish that the open source developers of SELinux could do something to make much more friendlier to use? Or maybe, some way that let's the user know what to do instead of letting the user `chmod`-ing and `chown`-ing files and directories endlessly. Or worse, completely disabling SELinux!

Hope you found this article interesting!

Stay tuned for more.
