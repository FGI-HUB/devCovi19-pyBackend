from rest_framework.permissions import AllowAny
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import News
from utils import *


class NewsSerializer(serializers.ModelSerializer):
    pictures = serializers.SerializerMethodField()

    def get_pictures(self, instance):
        """
            Get at pictures for all news
        """
        pics = []
        s = instance

        if s.picture:
            pics = get_upload_host(self.context["request"]) + s.picture.url

        # if s.picture:
        #     pics.append(get_upload_host(self.context["request"]) + s.picture.url)
        # if s.picture_thumbnail:
        #     pics.append(get_upload_host(self.context["request"]) + s.picture_thumbnail.url)

        return pics

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'pictures', 'created_date',)


class HomeNewsAPIView(APIView):

    def get(self, request, format=None):
        articles = News.objects.all()
        serializer = NewsSerializer(articles, many=True, context={"request":request})
        return Response(serializer.data)


