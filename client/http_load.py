import random
import string

from locust import HttpLocust, TaskSet


def execute(l):
    from gevent.pool import Group
    letters = string.ascii_lowercase
    key = random.randrange(0, 1000)
    second_key = random.randrange(0, 1000)
    value = ''.join(random.choice(letters) for i in range(10))
    group = Group()
    group.spawn(lambda:  l.client.get(f"/set/{key}/{value}"))
    group.spawn(lambda: l.client.get(f"/get/{second_key}"))
    group.join()


class UserBehavior(TaskSet):
    tasks = {execute: 1}

    def on_start(self):
        execute(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0
