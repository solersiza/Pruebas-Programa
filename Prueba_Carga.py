from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 3)  # espera aleatoria entre peticiones

    @task
    def index(self):
        self.client.get("/")
