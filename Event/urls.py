from Event import views
from django.conf.urls import url
urlpatterns = [
    url(r'^get_event/(?P<event_id>[0-9]+)/$', views.geteventdata, name='get'),
    url(r'^register/(?P<eventid>[0-9]+)/$', views.register_single, name='register_single'),
    url(r'^register/(?P<eventid>[0-9]+)/(?P<teamid>[0-9]+)/$', views.register_team, name='register_team'),
    # url(r'^notify/(?P<notification_id>[0-9]+)/$', views.getnotificationdata, name='notifications'),
    # url(r'^category/(?P<category>.*)/$', views.categorywise, name='get'),
    url(r'^summary/$', views.summary, name='summary'),
]
