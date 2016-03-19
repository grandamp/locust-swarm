#!/usr/bin/python

from locust import HttpLocust, TaskSet, task
from time import gmtime, strftime

import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (65536, 65536))

import requests
requests.packages.urllib3.disable_warnings()

class MyTaskSet(TaskSet):

    @task
    def validate(self):
        self.client.get("/")

        
class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait=1000
    max_wait=8000
