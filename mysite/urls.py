"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from app import views
from django.views.generic import TemplateView

from django.contrib.auth.views import login, logout

from django.conf.urls import include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'publishers', views.PublisherViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,5})/$', views.hours_ahead),
    url('^about/$', TemplateView.as_view(template_name= 'about.html')),
    url(r'^publishers/$', views.PublisherListView.as_view()),

    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),

    url('api/', include(router.urls)),
]
