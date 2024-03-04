

from django.urls import path
from content.views import Main, UploadFeed, Profile

urlpatterns = [
    path('content/upload', UploadFeed.as_view()),
    path('profile', Profile.as_view())
]

