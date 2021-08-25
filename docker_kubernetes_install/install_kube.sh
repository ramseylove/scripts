# script to install kubeadm kubeadm and kubectl

#install gpg key
sudo curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
#asks for password


# add repository
cat << EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF

# run update
sudo apt-get update

# Install packages
sudo apt-get install -y kubelet=1.15.7-00 kubeadm=1.15.7-00 kubectl=1.15.7-00

# Freeze versions of kube apps
sudo apt-mark hold kubelet kubeadm kubectl
#kubelet set on hold.
#kubeadm set on hold.
#kubectl set on hold.

# Check to see if install worked
kubeadm version
#kubeadm version: &version.Info{Major:"1", Minor:"15", GitVersion:"v1.15.7", GitCommit:"6c143d35bb11d74970e7bc0b6c45b6bfdffc0bd4", GitTreeState:"clean", BuildDate:"2019-12-11T12:40:15Z", GoVersion:"go1.12.12", Compiler:"gc", Platform:"linux/amd64"}

# if master
sudo kubeadm init --pod-network-cidr=10.244.0.0/16

# run as regular user
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# check to see if server communication is working
kubectl version
