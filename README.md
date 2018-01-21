# Flask-Vagrant-Setup
Configures a Flask app on a VM using [Vagrant](https://www.vagrantup.com/), accessible via [nginx](https://nginx.org/en/), and all orchestrated by [Ansible](https://www.ansible.com/).

## Prerequisite
You need to install:

- [Vagrant](https://www.vagrantup.com/downloads.html)

I will be using [VirtualBox](https://www.virtualbox.org/wiki/VirtualBox) for this setup, you can grab a copy for your OS [here](https://www.virtualbox.org/wiki/Downloads).

### Qucik start

1. clone this repo: 
 ```
 git clone https://github.com/clovisphere/Flask-Vagrant-Setup.git
 ```
2. Boot up your Vagrant environment:
```
vagrant up
```

_This may take less or more than a minute depending on your internet connection (so be patient)._ 

Vagrant runs the virtual machine without a UI. To prove that it is running, you can SSH into the machine:
```
vagrant ssh
```
You'd be see a welcome message like:
```
Welcome to Ubuntu 14.04.5 LTS (GNU/Linux 3.13.0-139-generic x86_64)
```

Now logout with: `logout`

### Access app

Navigate to: [10.0.0.5](http://10.0.0.5), you'd see a fancy "Hello" message:-)

