from locust import events
import logging

from locust.event import EventHook


@events.spawning_complete.add_listener
def spawn_users(user_count, **kwargs):
    print("Amount of users spawned:", user_count)

custom_locust_event = EventHook()

def custom_event(i, j, req_id, message=None, **kwargs):
    print(message)

custom_locust_event.add_listener(custom_event)