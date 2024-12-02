from locust import HttpUser, task, between
from Templates.CookieHttpTemplate import post_cookies, get_cookies, get_cookies_by_food


class ApiUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_cookies(self):
        get_cookies(self)

    @task
    def post_cookies(self):
        post_cookies(self)

    @task
    def get_cookies_by_food(self):
        get_cookies_by_food(self)
