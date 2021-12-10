from django.core.mail import send_mail
from bucket import bucket

from celery import shared_task
from celery_progress.backend import ProgressRecorder
from time import sleep


def get_objects_list_tasks():
    return bucket.get_objects


@shared_task
def delete_object_tasks(key):
    return bucket.delete_object(key)


@shared_task
def download_object_tasks(key):
    return bucket.download_object(key)


@shared_task
def send_email_task():
    send_mail(
        "Celery task worked",
        "This is proof the task worked",
        "shayan.aimoradii@gmail.com",
        ["redbull.9248@gmail.com"],
        fail_silently=False,
    )
    return None


@shared_task(bind=True)
def go_to_sleep(self, duration):
    progress_recorder = ProgressRecorder(self)
    for i in range(5):
        sleep(duration)
        progress_recorder.set_progress(i + 1, 5, f"On iteration {i}")
    return "Done"
