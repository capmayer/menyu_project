from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    #url(r'^menu/$', views.MenuList.as_view()),
    url(r'^menu/(?P<uuid>[^/]+)/$', views.MenuDetail.as_view()),
    url(r'^product/(?P<uuid>[^/]+)/$', views.ProductDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
