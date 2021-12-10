from django.conf import settings

import boto3


class Bucket:
    def __init__(self, *args, **kwargs):
        session = boto3.session.Session()

        self.conn = session.client(
            service_name="s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        )

    def get_objects(self):
        keys = []
        res = self.conn.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
        if res["KeyCount"]:
            return res["Contents"]
        return None

    def delete_object(self, key):
        self.conn.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=key)

    def download_object(self, key):
        with open(settings.AWS_STORAGE_BUCKET_NAME + key, "wb") as f:
            self.conn.download_fileobj(settings.AWS_STORAGE_BUCKET_NAME, key, f)


bucket = Bucket()
