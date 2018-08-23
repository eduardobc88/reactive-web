from django.conf.urls import url
from django.conf.urls import include
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^projects/$', views.ArchiveProjectListView.as_view(), name='project-archive'),
    url(r'^projects/(?P<page>\d+)/$', views.ArchiveProjectListView.as_view(), name='project-archive'),
    url(r'^projects/(?P<slug>[-\w]+)/$', views.ArchiveProjectDetailView.as_view(), name='project-detail'),
    url(r'^services/$', views.ArchiveServiceListView.as_view(), name='service-archive'),
    url(r'^services/(?P<page>\d+)/$', views.ArchiveServiceListView.as_view(), name='service-archive'),
    url(r'^services/(?P<slug>[-\w]+)/$', views.ArchiveServiceDetailView.as_view(), name='service-detail'),
    url(r'^blog/$', views.ArchivePostListView.as_view(), name='blog-archive'),
    url(r'^blog/(?P<page>\d+)/$', views.ArchivePostListView.as_view(), name='blog-archive'),
    url(r'^blog/(?P<slug>[-\w]+)/$', views.ArchivePostDetailView.as_view(), name='blog-detail'),
    # url(r'^gracias/$', views.thanks, name='thankyou-page'),
    url(r'^(?P<slug>[-\w]+)/$', views.PageDetailView.as_view(), name='page-detail'),
]
