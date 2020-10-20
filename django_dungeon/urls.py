from django.contrib import admin
from django.urls import path, include, url
from rooms.views import index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    path(r'^$', index),
]
