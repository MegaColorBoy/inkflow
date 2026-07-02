title: Install Docker on Fedora 35/36
date: October 1st, 2022
slug: install-docker-on-fedora-3536
category: DevOps + Linux + Docker
status: active

Recently, I started to play around with Docker and I thought of installing on my personal laptop which runs Fedora 36 workstation.

If you have Fedora and want to know how to install it, here it is:

## Install Docker Engine
First, add the official Docker repositories to your Fedora OS:

```bash
sudo dnf install dnf-plugins-core -y
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```

Then, you can run the following command to install Docker and it's dependencies:
```bash
sudo dnf install docker-ce docker-ce-cli containerd.io
```

During installation, you'll be prompted to import the GPG key in order to install Docker on your system. So, press <kbd>Y</kbd> to proceed with the installation.

Next, enable and start the docker service:

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

That's it you are done. You can try running the following command to see if it's installed properly on your system:
```bash
sudo docker run hello-world
```

If it works fine, you should be seeing a "Hello from Docker!" message which means that the installation appears to be working fine.

Hope you found this tutorial useful!
