from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    location = "media"


class StaticStorage(S3Boto3Storage):
    location = "static"
