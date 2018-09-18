# Flask-Vagrant-Setup
Configure a Flask app on a VM using [Vagrant](https://www.vagrantup.com/), with provisioning handled by [Ansible](https://www.ansible.com/) i.e _setting up [python](https://www.python.org/), [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/), [nginx](https://nginx.org/en/), [gunicorn](http://gunicorn.org/), etc._

## Prerequisite
You need to install:
- [Git](https://git-scm.com/)
- [Vagrant](https://www.vagrantup.com/downloads.html)

I will be using [VirtualBox](https://www.virtualbox.org/wiki/VirtualBox) for this setup, you can grab a copy for your OS [here](https://www.virtualbox.org/wiki/Downloads).

### Quick start
1. clone this repo and [cd](https://www.wikiwand.com/en/Cd_(command)) into it: 
 ```
 git clone git@github.com:clovisphere/Flask-Vagrant-Setup.git && cd Flask-Vagrant-Setup
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
You'd be seeing a welcome message like:
```
Welcome to Ubuntu 14.04.5 LTS (GNU/Linux 3.13.0-139-generic x86_64)
.
.
.
.
```

Now logout by typing: `logout`

### Access app
Point your browser to: [http://10.0.0.5](http://10.0.0.5), you'd see a fancy "Hello" message:-)


##### Credit
* [Aaron Oxborrow](https://github.com/paste), without whom I would have spent many more hours trying to understand *vagrant-ansible* provisioning.
