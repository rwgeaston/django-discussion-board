from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    url(r'^_nested_admin/', include('nested_admin.urls')),
    url(r'^auth/', include('social_django.urls', namespace='social')),
]
