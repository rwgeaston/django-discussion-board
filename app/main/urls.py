from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework_nested.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from discussion_board.views import UserViewSet
from discussion_board.views import EntityViewSet
from discussion_board.views import ThreadViewSet
from discussion_board.views import MessageViewSet
from discussion_board.views import EntityThreadViewSet
from discussion_board.views import UserThreadViewSet
from discussion_board.views import UserOwnedThreadViewSet
from discussion_board.views import UserMessageViewSet
from discussion_board.views import ThreadMessageViewSet


drf_api = SimpleRouter()
drf_api.register('users', UserViewSet)
drf_api.register('entities', EntityViewSet)
drf_api.register('threads', ThreadViewSet)
drf_api.register('messages', MessageViewSet)

entity_router = NestedSimpleRouter(drf_api, 'entities', lookup='entity')
entity_router.register('threads', EntityThreadViewSet, base_name='entity-threads')

user_router = NestedSimpleRouter(drf_api, 'users', lookup='user')
user_router.register('threads', UserThreadViewSet, base_name='user-threads')
user_router.register('owned_threads', UserOwnedThreadViewSet, base_name='user-owned-threads')
user_router.register('messages', UserMessageViewSet, base_name='user-messages')

thread_router = NestedSimpleRouter(drf_api, 'threads', lookup='thread')
thread_router.register('messages', ThreadMessageViewSet, base_name='thread-messages')

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    url(r'^_nested_admin/', include('nested_admin.urls')),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url('api/', include(drf_api.urls)),
    url('api/', include(entity_router.urls)),
    url('api/', include(user_router.urls)),
    url('api/', include(thread_router.urls)),
]
