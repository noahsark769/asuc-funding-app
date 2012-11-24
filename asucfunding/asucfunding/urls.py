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
    url(r'^update_config/$', 'funding_app.views.change_config'),
    url(r'^process_calnet/$', 'funding_app.views.process_calnet'),
    url(r'^logout/$', 'funding_app.views.logout'),
    url(r'^create_request/$', 'funding_app.views.submitter_render_funding_request'),
    url(r'^edit_request/(?P<request_id>\w{1,50})/$', 'funding_app.views.submitter_render_funding_request'),
    url(r'^review_request/$', 'funding_app.views.submitter_render_funding_request'),
    url(r'^admin_review_request/$', 'funding_app.views.admin_render_funding_request'),
    url(r'^admin_award_request/$', 'funding_app.views.admin_render_funding_request'),
    url(r'^export_to_excel/$', 'funding_app.views.admin_export_to_excel')
)
