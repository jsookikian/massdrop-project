#!/usr/bin/env bash

# Amazon EC-2 Instance setup script
yum install python36
virtualenv flask-env
source flask-env/bin/activate
sudo pip-3.6 install -r requirements.txt



