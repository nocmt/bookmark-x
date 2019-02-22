from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Bookmarks, Sort
from .serializer import BookmarksSerializer, SortsSerializer

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

# 使用APIView
class BookmarksView(APIView):
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
