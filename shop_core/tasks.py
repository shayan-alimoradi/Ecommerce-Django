from bucket import bucket

from celery import shared_task


def get_objects_list_tasks():
    return bucket.get_objects


@shared_task
def delete_object_tasks(key):
    return bucket.delete_object(key)


@shared_task
def download_object_tasks(key):
    return bucket.download_object(key)