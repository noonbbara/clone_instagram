

from django.urls import path
from content.views import Main, UploadFeed

urlpatterns = [
    path('content/upload', UploadFeed.as_view()),
]

