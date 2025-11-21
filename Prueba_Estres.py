from locust import HttpUser, task, between, events
from locust.runners import STATE_STOPPING, STATE_STOPPED, STATE_CLEANUP
import gevent

class StressTestUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index(self):
        self.client.get("/")


@events.quitting.add_listener
def _(environment, **kw):
    stats = environment.stats.total
    if stats.fail_ratio > 0.10:  
        print("❌ Alto nivel de fallos detectado.")
    else:
        print("✔ Prueba finalizada con estabilidad aceptable.")
