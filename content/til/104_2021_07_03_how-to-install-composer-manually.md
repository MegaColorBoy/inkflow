title: How to install Composer manually?
date: July 3rd, 2021
slug: how-to-install-composer-manually
category: Tooling
status: active

You may wonder **"why not install Composer via apt or yum package manager?"** and yes, it can be installed that way too.

But what if you are using old composer packages or you wanted to skip the checks done during the interactive installation routine, this could be the way for you.

I wouldn't really call it an advanced technique or something but if you know what you're doing, then you should be in the right direction.

The below snippet will show you how to install it manually:
```bash
wget "https://getcomposer.org/download/VERSION_X.X.X/composer.phar"
sudo mv composer.phar /usr/local/bin/composer
sudo chmod a+x /usr/local/bin/composer
```

## Yes, that's it!
By placing Composer in the `/usr/local/bin` directory, it will be accessible from any directory within the system and you can run it globally.

To check if you've installed it correctly, just do the following:
```bash
composer -V
```

Hope you found this tip useful!