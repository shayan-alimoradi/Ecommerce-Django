from django.urls import path
from . import views

app_name = "core"


urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("progress/", views.ProgressBar.as_view(), name="progress"),
    path("bucket-list/", views.BucketList.as_view(), name="bucket_list"),
    path(
        "delete-bucket/<str:key>/", views.DeleteBucket.as_view(), name="delete_bucket"
    ),
    path(
        "download-bucket/<str:key>/",
        views.DownloadBucket.as_view(),
        name="download_bucket",
    ),
]
