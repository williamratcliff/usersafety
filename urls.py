from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings
REPO_ROOT=settings.REPO_ROOT

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'psdplan.views.home', name='home'),
    # url(r'^psdplan/', include('psdplan.foo.urls')),
    #url(r'^$', 'psdplan.apps.viewpsd.views.home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'', include('registration.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns(REPO_ROOT + '.apps.activation_analysis.views',
                        ('^activation/$', 'activation_view'),
                        #('^$', 'home'),     
                        )

urlpatterns += patterns(REPO_ROOT + '.apps.viewpsd.views',
                        ('^psd$', 'psd'), 
                        ('^calculate/$', 'calculate'), 
                        ('^$', 'home'),                                                      
                        )

