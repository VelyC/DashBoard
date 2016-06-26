from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.login_page, name='login'),
   url(r'^logout$', views.logout_page, name='logout'),
   url(r'^signup$', views.new_user, name='signup'),
]
