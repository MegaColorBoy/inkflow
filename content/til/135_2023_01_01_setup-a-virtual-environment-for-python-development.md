title: Setup a virtual environment for Python development
date: January 3rd, 2023
slug: setup-a-virtual-environment-for-python-development
category: Python
status: active

`virtualenv` is a tool used that allows you to install and isolate Python packages that are specific to your project rather than installing them globally on your system, which might, at some point, break other tools or services in your system.

In this simple guide, I'll show you how to install and create your own Python virtual environment for development.

Before you begin, please make sure that you have installed Python 3 or greater on your system.

## Install virtualenv

Using the `pip` tool, you can execute the following command:

```bash
sudo pip install virtualenvwrapper
```

Then you need to add the following lines to your `.bashrc` startup file (found in the home directory).

These lines determine where your virtual environments should live, the location of the script installed and the location of the development project directories:

```bash
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

Next, restart the startup file:

```bash
source .bashrc
```

Once done, it'l execute a bunch of scripts for a few minutes and once the installation is successful, you can start using the `mkvirtualenv` command to create your virtual environment.

## Creating a virtual environment

Really, it's quite trivial to create a virtual environment like this:

```bash
mkvirtualenv my_virtual_environment
```

Once done, you'll notice that your terminal looks something like this:

```text
(my_virtual_environment) user@desktop:~$
```

This indicates that you are inside the virtual environment and can begin installing your Python packages and begin developing your application.

## Using the virtual environment

There are a few commands that I'd like to share (and you should also know) while working with a virtual environment:

- `deactivate` &mdash; get out of the current virtual environment
- `workon` &mdash; list available virtual environments on the system
- `workon name_of_environment` &mdash; activate the specified virtual environment
- `rmvirtualenv name_of_environment` &mdash; remove the specified virtual environment

## Conclusion

If you are a Python developer or write code in Python, then virtual environments are super handy and disposable especially while testing and working on different projects.

Unless, your project is package-dependant, you don't really need to isolate your development environment.

Hope you found this article useful!
