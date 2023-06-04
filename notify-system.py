import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Hey!, ",
            message="You are a very Hard worker man, it's been a hour, Take a Break...",
            timeout=10
        )
        time.sleep(3600)