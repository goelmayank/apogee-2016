from registrations import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.home),
    url(r'^papers/instructions/$', views.papersInstructions),
    url(r'^papers/form/$', views.papersForm),
    url(r'^papers/status/$', views.papersStatus),
    url(r'^projects/instructions/$', views.projectsInstructions),
    url(r'^projects/status/$', views.projectsStatus),
    url(r'^projects/form/$', views.projectsForm),
    url(r'^check/form/$', views.checkForm),
    url(r'^check/status/$', views.checkStatus),
        


    #url(r'^username/set/(?P<user_id>\d+)/$', views.username_set),
    #url(r'^username/save/(?P<user_id>\d+)/$', views.username_save),
    #url(r'^dashboard/$', views.dashboard, name='dashboard'),
    #url(r'^changelimit/$', views.change_team_limits),
    #url(r'^change_team_limit/$', views.change_team_limit_list),
    #url(r'^limit_changed/$', views.change_limits),
    #url(r'^sportlimit/select/$', views.sportlimit_select, name='sportlimits'),
    #url(r'^sportlimit/change/$', views.sportlimit_change),
    #url(r'^sportlimit/save/$', views.sportlimit_save),
    #url(r'^email/select/$', views.email_select),
    #url(r'^email/compose/$', views.email_compose),
    #url(r'^email/statchange/$', views.email_statchange, name='statchange'),
    #url(r'^email/send/$', views.email_send),
    #url(r'^status/select/$', views.status_select),
    #url(r'^status/set/$', views.status_set),
    #url(r'^status/save/$', views.status_save),
    #url(r'^logout/$', views.user_logout),
    # url(r'^sports_limits_changed/$', views.save_sports_limits),
    # url(r'^setstatus/$', views.set_status),
    # url(r'^showstatus/$', views.save_status),
    #url(r'^emailsend/$', views.send_mail),
    # url(r'^compose/$', views.compose),
    #url(r'^listuser/$', views.user_list),
    #url(r'^participantlist/$', views.participant_list),
    #url(r'^users/$', views.search_user),
    #url(r'^participants/$', views.search_plist),
    #url(r'^pconfirm/$', views.pconfirm),
    #url(r'^pedit$', views.pedit), 
    #url(r'^stats/$', views.stats_view, name='stats'),
    #url(r'^stats/college/(?P<userid>\d+)/$', views.stats_college, name='stats_college'),
    #url(r'^stats/event/(?P<eventid>\d+)/$', views.stats_event, name='stats_event'),
    #url(r'^loginas/warning/$', views.loginas_warning),
    #url(r'^loginas/select/$', views.loginas_select),
    #url(r'^loginas/user/(?P<userid>\d+)/$', views.loginas_login),
    # url(r'^(?P<pagename>\w+)/', views.pathfinder),
    ]
