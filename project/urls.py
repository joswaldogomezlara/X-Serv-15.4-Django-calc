from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^(?P<num1>[0-9]+)\+(?P<num2>[0-9]+)/$', 'calc.views.sumar'),
    url(r'^(?P<num1>[0-9]+)\-(?P<num2>[0-9]+)/$', 'calc.views.restar'),
    url(r'^(?P<num1>[0-9]+)\*(?P<num2>[0-9]+)/$', 'calc.views.multiplicar'),
    url(r'^(?P<num1>[0-9]+)\/(?P<num2>[0-9]+)/$', 'calc.views.dividir'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'.*', 'calc.views.NotFound'),
)
