from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.signin, name='signin'),
   url(r'^signout$', views.signout, name='signout'),
   url(r'^signup$', views.signup, name='signup'),
   url(r'^missionary/overview$', views.missionary_overview, name='overview'),
   url(r'^missionary/add$', views.missionary_add, name='addmiss'),
   url(r'^missionary/modify$', views.missionary_modify, name='modifymiss'),
]
