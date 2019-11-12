import random
import string

from locust import HttpLocust, TaskSet


def set(l):
    letters = string.ascii_lowercase
    key = random.randrange(0, 1000)
    value = ''.join(random.choice(letters) for i in range(10))
    l.client.get(f"/set/{key}/{value}")


def get(l):
    key = random.randrange(0, 1000)
    l.client.get(f"/get/{key}")


class UserBehavior(TaskSet):
    tasks = {set: 1, get: 1}

    def on_start(self):
        set(self)

    def on_stop(self):
        get(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0
