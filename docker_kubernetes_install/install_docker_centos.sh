# remove old versions of docker from the machine
sudo yum remove -y docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine

# Install utilities first
sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2

# setup stable repository
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

#install docker CE
sudo yum -y install docker-ce

#enable and start docker 
sudo systemctl start docker && sudo systemctl enable docker

# add cloud_user to the docker group
sudo usermod -aG docker cloud_user
