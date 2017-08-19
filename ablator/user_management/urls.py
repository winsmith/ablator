from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'users/create/$', views.UserCreate.as_view(), name='user-create'),
    url(r'users/update/(?P<pk>[^/]+)/$', views.UserUpdate.as_view(), name='user-update'),
    url(r'users/delete/(?P<pk>[^/]+)/$', views.UserDelete.as_view(), name='user-delete'),
    url(r'$', views.UserList.as_view(), name='user-list'),
]
