title: Getting started with Laravel Homestead
date: November 16th, 2019
slug: getting-started-with-laravel-homestead
category: Tutorial
summary: Wanted to install Laravel but scared of configuring files on your host operating system? This article is for you.

I started learning Laravel and I thought of writing a small tutorial on how to setup your own local development environment for Laravel projects with Laravel Homestead and Vagrant.

## What is Laravel Homestead?
It's an official package from Laravel that provides a neat development environment that comes along with a Vagrant box that has pre-installed software. Read their [documentation](https://laravel.com/docs/6.x/homestead) to know more about it.

**Note:** The examples of this tutorial are applicable to any developer that uses any UNIX-based operating systems such as macOS or any Linux distributions like Ubuntu. If you're using Windows, I recommend that you install [Git for Windows](https://gitforwindows.org) on your local machine.

## Prerequisites
The only requirement for this tutorial is that you should be familiar with using the command-line interface.

## Install VirtualBox and Vagrant
[VirtualBox](https://virtualbox.org) is the software used to run a virtual machine with a sandbox operating system within your own computer.

[Vagrant](https://vagrantup.com) is a software that's used to manage a development environment. Through the command-line, you can perform any operation such as installing an OS, configuration, deployment and so on.

You can install VirtualBox and Vagrant via the command-line:
```bash
sudo apt install virtualbox vagrant
```

Once you're done installing them, you should add the <mark>laravel/homestead</mark> box to your Vagrant installation using the following command:
```bash
vagrant box add laravel/homestead
```

To check if it has been installed, use the following command:
```bash
vagrant box list | grep "homestead"
```

Using VirtualBox and Vagrant allows you to simulate your Laravel development environment without messing up any configurations on your hosting system. Even if you did, no worries, Vagrant boxes are disposable, so you can destroy and create a new box again in minutes.

## Download Laravel Homestead
You can install Homestead by cloning it's repository onto your local machine by typing the following command:

```bash
git clone https://github.com/laravel/homestead.git ~/projects/Homestead
```

### Generate configuration file
Once you're done cloning the repository, go inside the <mark>projects/Homestead</mark> directory and run the <mark>init.sh</mark> or <mark>init.bat</mark> (for Windows) to create the <mark>Homestead.yaml</mark> configuration file:

```bash
cd projects/Homestead
bash init.sh
```

Open the default <mark>Homestead.yaml</mark> file and make the following changes:
```yaml
---
ip: "192.168.10.10"
memory: 2048
cpus: 2
provider: virtualbox

authorize: ~/.ssh/id_rsa.pub

keys:
    - ~/.ssh/id_rsa

folders:
    - map: ~/projects/code
      to: /home/vagrant/projects/code

sites:
    - map: homestead.test
      to: /home/vagrant/projects/code/public

databases:
    - homestead
```

### Generate SSH key
The documentation for Laravel Homestead doesn't really talk about generating SSH keys used to access the Vagrant box. Use the following command to generate it using <mark>ssh-keygen</mark> on the command-line:

```bash
ssh-keygen -t rsa -C "root@homestead"
```

### Map the project's shared folder
Make sure that you have created a folder named <mark>code</mark> in your <mark>projects</mark> directory. This folder will keep all of your Laravel project files in sync between your local machine and Homestead environment.

## Installing Laravel
Time to install Laravel into your virtual machine. So, get switch on your virtual machine by doing the following in the command-line:

```bash
vagrant up
```

As you're switching it on for the first time, depending on your internet connection, it might take somewhere around 10-20 minutes to getting it running but it'll be fine afterwards.

Alright, login to your Vagrant machine by doing the following the command-line:
```bash
vagrant ssh
```

Once you're in, go to your <mark>code</mark> directory and type the following in the command-line:
```bash
composer global require laravel/installer
```

## Create a new project
Now, it's time to create a new Laravel project by simply typing the following command:
```bash
laravel new projectname
```
It'll take some time to generate the necessary files and boilerplate code and after that, you're good to go!

Oh, you should be able to see the Laravel project files in your local machine as it's synced with the virtual machine and local machine. That means, any changes made on either machines will be synced and reflected on both ends.

## Map your hosts file
One last step, make sure you map your project's test domain onto your local machine's <mark>hosts</mark> file.

Open a text-editor of your choice and do the following in the <mark>etc/hosts</mark> file:
```text
127.0.0.1   localhost
::1         localhost

# Add this line (Note: It can be any URL)
127.0.0.1   homestead.test
```
Now, go to your browser and type <mark>homestead.test</mark> and you should be able to see your Laravel project's sample layout.

## Conclusion
As mentioned, in the beginning of this article, I have started to learn Laravel and I'll be building some projects and writing out my experiences about it soon.

I hope you liked reading this article and please share it with others if you do find this tutorial useful.

Stay tuned for more!