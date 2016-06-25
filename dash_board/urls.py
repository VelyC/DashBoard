from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.login_page, name='login'),
   url(r'^main$', views.main, name='main'),
   url(r'^signup$', views.new_user, name='signup'),
]
