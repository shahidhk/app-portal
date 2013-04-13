from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'application_portal.views.home', name='home'),
    url(r'^dashboard/', 'core.views.core_dashboard', name='core_home'),
    url(r'^subdepartments/','core.views.subdepartments',name='core_subdepartments'),
    url(r'^questions/','core.views.questions',name='core_questions'),
    url(r'^submissions/','core.views.submissions',name='core_submissions'),
    url(r'^applicants/','core.views.applicants',name='core_applicants'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

