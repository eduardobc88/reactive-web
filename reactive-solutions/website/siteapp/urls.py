from django.conf.urls import url
from django.conf.urls import include
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ArchiveBlogSitemap, PageSitemap, ArchiveProjectSitemap, ArchiveServiceSitemap
from django.urls import path


sitemaps = {
    'Pages': PageSitemap,
    'Services': ArchiveServiceSitemap,
    'Projects': ArchiveProjectSitemap,
    'Blog': ArchiveBlogSitemap,
}


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^proyectos/$', views.ArchiveProjectListView.as_view(), name='project-archive'),
    url(r'^proyectos/(?P<page>\d+)/$', views.ArchiveProjectListView.as_view(), name='project-archive'),
    url(r'^proyectos/(?P<slug>[-\w]+)/$', views.ArchiveProjectDetailView.as_view(), name='project-detail'),
    url(r'^servicios/$', views.ArchiveServiceListView.as_view(), name='service-archive'),
    url(r'^servicios/(?P<page>\d+)/$', views.ArchiveServiceListView.as_view(), name='service-archive'),
    url(r'^servicios/(?P<slug>[-\w]+)/$', views.ArchiveServiceDetailView.as_view(), name='service-detail'),
    url(r'^blog/$', views.ArchivePostListView.as_view(), name='blog-archive'),
    url(r'^blog/(?P<page>\d+)/$', views.ArchivePostListView.as_view(), name='blog-archive'),
    url(r'^blog/(?P<slug>[-\w]+)/$', views.ArchivePostDetailView.as_view(), name='blog-detail'),
    url(r'^gracias/$', views.thanks, name='thankyou-page'),
    url(r'^sitemap.xml/$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^(?P<slug>[-\w]+)/$', views.PageDetailView.as_view(), name='page-detail'),
]
