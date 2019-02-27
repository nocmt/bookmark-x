from rest_framework import serializers

from .models import *


# 用于注册的时候返回json数据
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = []
        model = Users
        EaddTime = serializers.ReadOnlyField()
        field = ('id', 'username', 'EaddTime')


class UserSerializer(serializers.ModelSerializer):
    # bookmarks_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Bookmarks.objects.all())
    class Meta:
        exclude = []
        model = Users
        EaddTime = serializers.ReadOnlyField()
        field = ('id', 'username', 'EaddTime')


class BookmarksSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = []
        sortName = serializers.ReadOnlyField()
        EaddTime = serializers.ReadOnlyField()
        model = Bookmarks
        fields = ('id', 'user', 'title', 'link', 'imgUrl', 'sortName', 'EaddTime', 'isInvalid')


class SortsSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = []
        model = Sort
        EaddTime = serializers.ReadOnlyField()
        fields = ('id', 'user', 'name', 'EaddTime', 'isEnable')
