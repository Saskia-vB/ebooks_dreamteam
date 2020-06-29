
Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/xenial64"
  config.vm.synced_folder("app", "/app")
  config.vm.provision "shell", path: "provision.sh"

end
