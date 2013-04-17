from django.conf.urls import patterns, include, url
import safetylist.views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nistproject.views.home', name='home'),
    # url(r'^nistproject/', include('nistproject.foo.urls')),
    url(r'^$', safetylist.views.addcontact, name='add'),
    url(r'^list', safetylist.views.listcontact, name='list'),
    url(r'^(?P<pk>\d+)/$', safetylist.views.detailcontact, name='detail'),
#    url(r'^detail', safetylist.views.detailcontact, name='detail'),    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
