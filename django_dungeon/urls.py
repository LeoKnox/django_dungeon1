from django.contrib import admin
from django.conf.urls import include, url
from rooms.views import index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
]
