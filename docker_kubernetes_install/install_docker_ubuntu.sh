# this is script is desinged to install docker on a remote machine via ssh
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
#[sudo] password for cloud_user:
# PRompt

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
#Prompt

sudo apt-get update -y
#Prompt

sudo apt-get install -y docker-ce=18.06.1~ce~3-0~ubuntu
#Prompt

sudo apt-mark hold docker-ce
#Prompt

#test to confirm successful installation
sudo docker version
