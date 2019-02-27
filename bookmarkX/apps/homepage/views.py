from __future__ import unicode_literals

from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import *
from .serializer import BookmarksSerializer, SortsSerializer, UserSerializer, UserRegisterSerializer

from django.http import QueryDict
from rest_framework.request import Request


# 解析request参数
def get_parameter_dic(request, *args, **kwargs):
    if isinstance(request, Request) == False:
        return {}

    query_params = request.query_params
    if isinstance(query_params, QueryDict):
        query_params = query_params.dict()
    result_data = request.data
    if isinstance(result_data, QueryDict):
        result_data = result_data.dict()

    if query_params != {}:
        return query_params
    else:
        return result_data


class BookmarksView(APIView):
    queryset = Bookmarks.objects.all()
    serializer_class = BookmarksSerializer
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        params = get_parameter_dic(request)
        sort = Sort.objects.filter(name=params.get('sort'))
        if sort:
            bookmarks = Bookmarks.objects.filter(sort=sort[0])
        else:
            bookmarks = Bookmarks.objects.all()
        serializer = BookmarksSerializer(bookmarks, many=True)
        return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     data = request.data
    #
    #     serializer = BookmarksSerializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SortsView(APIView):
    def get(self, request, format=None):
        serializer = SortsSerializer(Sort.objects.all(), many=True)
        return Response(serializer.data)


# 用于登录
class UserLoginAPIView(APIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        params = get_parameter_dic(request)

        username = params.get('username')
        password = params.get('password')

        user = Users.objects.get(username__exact=username)
        # 校对密码
        if check_password(password, user.password):
            serializer = UserSerializer(user)
            new_data = serializer.data
            # 记忆已登录用户
            self.request.session['user_id'] = user.id
            return Response(new_data, status=HTTP_200_OK)
        return Response('password error', HTTP_400_BAD_REQUEST)


# 用于注册
class UserRegisterAPIView(APIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        params = get_parameter_dic(request)
        username = params.get('username')
        if Users.objects.filter(username__exact=username):
            return Response("用户名已存在", HTTP_400_BAD_REQUEST)
        params['password'] = make_password(params['password'])
        serializer = UserRegisterSerializer(data=params)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# 用于书签的增删改查  除了查看，其他都需要权限
# class BookmarksViewSet(viewsets.ModelViewSet):
#     queryset = Bookmarks.objects.all()
#     serializer_class = BookmarksSerializer
#     permission_classes = (IsAuthenticated,)
#
#     def perform_create(self, serializer):
#         print(self.request.user)
#         serializer.save(user=Users.objects.get(id=self.request.session.get('user_id')))


