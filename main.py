# python program to create a desk notifiaction that will tell you to drink water at regular intervals

import time

from plyer import notification

while True:
    notification.notify(
        title="Reminder about water",
        message="drink water",
        timeout=60
    )

    time.sleep(60*60)
