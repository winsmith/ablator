from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^v1/caniuse/(?P<client_user_string>[^/]+)/(?P<functionality_group_id>[^/]+)/?$', views.CanIUseSingleViewV1.as_view()),
    url(r'^v1/which/(?P<client_user_string>[^/]+)/(?P<functionality_group_id>[^/]+)/?$', views.WhichSingleViewV1.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
