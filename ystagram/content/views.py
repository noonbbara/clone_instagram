from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import Feed
import os
from django.conf import settings
from ystagram.settings import MEDIA_ROOT
from uuid import uuid4
# Create your views here.
class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')
        # select * from content_feed;

        for feed in feed_list:
            print(feed.content)
        return render(request, "ystagram/main.html", context=dict(feeds=feed_list))


class UploadFeed(APIView):
    def post(self, request):

        #파일 불러오기
        file = request.FILES['file']
        uuid_name = uuid4().hex #파일 이름을 서버에서 관리하기 쉽게 파일 이름 랜덤하게 설정
        save_path = os.path.join(settings.MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        image = uuid_name
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        Feed.objects.create(image=image, content=content, user_id=user_id, profile_image=profile_image, like_count=0)

        return Response(status=200)