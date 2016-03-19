#!/bin/bash

export AWS_SECRET_ACCESS_KEY=[REPLACE]
export AWS_ACCESS_KEY_ID=[REPLACE]
export ANSIBLE_HOST_KEY_CHECKING=False
cp agent.py roles/locust/templates
ansible-playbook -i aws_hosts.ini locust.yml --private-key [REPLACE]

