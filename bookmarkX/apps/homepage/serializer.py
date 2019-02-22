from rest_framework import serializers

from .models import Bookmarks, Sort


class BookmarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmarks
        fields = ('id', 'user', 'title', 'link', 'imgUrl', 'sort', 'addTime', 'isInvalid')


class SortsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sort
        fields = ('id', 'user', 'name', 'addTime', 'isEnable')
