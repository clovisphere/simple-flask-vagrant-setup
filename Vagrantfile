# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
VAGRANT_IP = "10.0.0.0"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network :private_network, ip: VAGRANT_IP

  # 
  # port forwarding to allow access to the app running on the guest OS
  # from a dedicated port on the host machine
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # run Ansible from the Vagrant VM
  config.vm.provision "ansible_local" do |ansible|
    ansible.install = true
    ansible.playbook = ".provisioning/playbook.yml"
    ansible.inventory_path = ".provisioning/inventory"
  end

  # add localhost to Ansible inventory
  config.vm.provision "shell", inline: "printf 'localhost\n' | sudo tee /etc/ansible/hosts > /dev/null"

  # increase VM RAM size
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end
end
