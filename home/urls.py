from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^intro/$', views.intro, name='intro'),
    url(r'^intro/about/$', views.my_info),
    url(r'^intro/home/$', views.menu_home),
    url(r'^about/$', views.my_info),
    url(r'^home/$', views.menu_home)
]
