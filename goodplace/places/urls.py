from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    url(r'^propose/(?P<prop_id>[0-9]+)/$', views.propose, name='propose'),

    url(r'^proplist/$', views.proplist, name='proplist')
]