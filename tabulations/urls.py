from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^tabulation/$', views.TabulationList.as_view()),
    url(r'^tabulation/(?P<uuid>[^/]+)/$', views.TabulationDetail.as_view()),
    url(r'^order/$', views.OrderList.as_view()),
    url(r'^order/(?P<uuid>[^/]+)/$', views.OrderDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
