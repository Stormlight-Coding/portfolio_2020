from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^support$', views.support),
    url(r'^algo$', views.algo),
    url(r'^barry$', views.barry),
    url(r'^list$', views.list),
    url(r'^numbers$', views.numbers),
    url(r'^strata$', views.strata),
    url(r'^wedding$', views.wedding),
]
