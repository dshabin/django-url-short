from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.shortner, name='shortner'),
    url(r'^!', views.show_info, name='show_info'),
    url(r'', views.resolver, name='resolver'),
]
