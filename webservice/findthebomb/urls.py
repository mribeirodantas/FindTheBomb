from django.conf.urls import patterns, include, url
from webservice.views import join_CT, join_TR, create_map, quit_match, plant_bomb, disarm_bomb

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'findthebomb.views.home', name='home'),
    # url(r'^findthebomb/', include('findthebomb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^create/(.*)', create_map),
    url(r'^join/ct/(.*)', join_CT),
    url(r'^join/tr/(.*)', join_TR),
    url(r'^quit/(.*)', quit_match),
    url(r'^plant/(.*)', plant_bomb),
    url(r'^disarm/(.*)', disarm_bomb),
)
