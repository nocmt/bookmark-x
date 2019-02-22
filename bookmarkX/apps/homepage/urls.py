from django.urls import path
from . import views

urlpatterns = [
    path('bookmarks', views.BookmarksView.as_view(), name='bookmarks'),
    path('sorts', views.SortsView.as_view(), name='sorts')
]
