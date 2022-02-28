#!/bin/bash

# update package repository
sudo yum update -y

# install git and java
sudo yum install git -y
sudo yum install java-1.8.0 -y

# docker install and start commands
sudo amazon-linux-extras install docker -y
sudo service docker start
sudo systemctl enable docker

# add ec2-user and jenkins users to docker group to be able to run "docker ..." instead of "sudo docker ...."
sudo usermod -a -G docker ec2-user
sudo usermod -a -G docker jenkins

# install terraform
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo yum -y install terraform


