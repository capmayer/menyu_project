"""menyu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, handler404
from django.contrib import admin
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('menus.urls')),
    url(r'^api/', include('tabulations.urls')),
    url(r'^api/', include('configs.urls')),
    url(r'^api/auth/login/', obtain_jwt_token),
    url(r'^api/auth/refresh/', refresh_jwt_token),
    url(r'^api/auth/verify/', verify_jwt_token),
    url(r'$^', include('home.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'home.views.facebook'
