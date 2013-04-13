from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'application_portal.views.home', name='home'),
    url(r'^$','core.views.urlhandler'),
    url(r'^(?P<username>\w+)/dashboard/', 'core.views.core_dashboard', name='core_home'),
    url(r'^(?P<username>\w+)/subdepartments/','core.views.subdepartments',name='core_subdepartments'),
    url(r'^(?P<username>\w+)/questions/','core.views.questions',name='core_questions'),
    url(r'^(?P<username>\w+)/submissions/','core.views.submissions',name='core_submissions'),
    url(r'^(?P<username>\w+)/applicants/','core.views.applicants',name='core_applicants'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

