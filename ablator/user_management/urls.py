from django.conf.urls import url
from django.urls.base import reverse

from . import views

urlpatterns = [
    url(r'create/$', views.UserCreate.as_view(), name='user-create'),
    url(r'$', views.UserList.as_view(), name='user-list'),
]