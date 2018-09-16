from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from discussion_board.views import UserViewSet
from discussion_board.views import EntityViewSet
from discussion_board.views import ThreadViewSet
from discussion_board.views import MessageViewSet


drf_api = DefaultRouter()
drf_api.register('users', UserViewSet)
drf_api.register('entities', EntityViewSet)
drf_api.register('threads', ThreadViewSet)
drf_api.register('messages', MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    url(r'^_nested_admin/', include('nested_admin.urls')),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url('api/', include(drf_api.urls))
]
