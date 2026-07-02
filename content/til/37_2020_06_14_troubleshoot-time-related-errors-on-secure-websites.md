title: Troubleshoot time-related SSL errors on secure websites
date: June 14th, 2020
slug: troubleshoot-time-related-ssl-errors-on-secure-websites
category: SSL
status: active

As I was configuring Arch Linux setup on my old HP 8460p laptop, I noticed that I wasn't able to access any site using Chrome or Firefox as I was faced with a weird error:

<!--- ![SSL Certificate Error](../../../static/til_images/ssl-time-error.png)-->
<img src="../../../static/til_images/ssl-time-error.png" style="width: 500px;" />

I was quite confused and thought it might be an issue with my WiFi card or probably some server issue but turns out it was neither of them.

On the side of my screen, I noticed my system time was displaying 4 hours ahead of the current local time, which is wrong. So, I did a little research and turns out my suspicions were correct, it's a time-related issue.

## How is time related to secure websites?
Well, each website that uses SSL or that begins with `https://` are only valid for a period of time before getting expired. If the website that you're trying to visit presents a certificate with a time and date that doesn't match with your system's clock, Firefox will prevent you from accessing the page.

## How to fix it?
Actually, the fix is quite simple. All you have to is just set the correct date and time on your system and you're good to go!

If you're using Linux, just do the following:

### 1. Set up your timezone
You can look up for your timezones by executing the following:
```bash
timedatectl list-timezones | less
```

Once, you've found your timezone, execute the following by replacing `Continent/Country` with your timezone:
```bash
timedatectl set-timezone Continent/Country
```

### 2. Manually set your local time
Execute the following to set up your time, locally on your system:
```bash
timedatectl set-time "yyyy-MM-dd hh:mm:ss"
```

### 3. Set the hardware clock from the system clock
The following command sets the hardware clock from the system clock:
```bash
hwclock --systohc
```

Now, that you've executed them, you should be able to view the correct time on your system by executing `timedatectl status` and you should see something like this:
```bash
               Local time: Sun 2020-06-14 21:04:04 +04
           Universal time: Sun 2020-06-14 17:04:04 UTC
                 RTC time: Sun 2020-06-14 17:04:05    
                Time zone: Asia/Dubai (+04, +0400)    
System clock synchronized: no                         
              NTP service: inactive 
```

Although, this issue was time-related, you may face the same kind of error for various other reasons. Try reading more on how to [troubleshoot](https://support.mozilla.org/en-US/kb/troubleshoot-time-errors-secure-websites) errors like these from Mozilla's official documentation.
