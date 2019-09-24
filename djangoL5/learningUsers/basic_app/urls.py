from django.conf.urls import url
from basic_app import views


# NB: since we are using template urls, we need to setup app name and
app_name = 'basic_app'                          #this has to match with the application name
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]
