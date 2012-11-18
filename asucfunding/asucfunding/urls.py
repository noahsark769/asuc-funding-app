from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asucfunding.views.home', name='home'),
    # url(r'^asucfunding/', include('asucfunding.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'funding_app.views.home'),
    url(r'^submitter/$', 'funding_app.views.submitter_request_summary'),
    url(r'^admin/$', 'funding_app.views.admin_request_summary'),
    url(r'^config/$', 'funding_app.views.config'),
<<<<<<< HEAD
    url(r'^update_config/$', 'funding_app.views.change_config'),
=======
    url(r'^process_calnet/', 'funding_app.views.process_calnet'),
    url(r'^logout/', 'funding_app.views.logout'),
>>>>>>> 916bc43b095ee27b7c089b39864df0efcf4a8b4b
)
