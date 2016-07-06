from django.conf.urls import url

##########################################################################
# User imports..
##########################################################################
from . import views

urlpatterns = [
   # 기본 페이지.
   url(r'^$', views.signin, name='signin'),
   # authentication 관련 페이지..
   url(r'^signout$', views.signout, name='signout'),
   url(r'^signup$', views.signup, name='signup'),
   # missionary 관련 페이지 ....
   url(r'^missionary/overview$', views.missionary_overview, name='overview'),
   url(r'^missionary/add$', views.missionary_add, name='addmiss'),
   url(r'^missionary/modify$', views.missionary_spread, name='spreadmiss'),
   url(r'^missionary/modify#(?P<pk>[0-9]+)$', views.missionary_modify, name='midifymiss'),
]
