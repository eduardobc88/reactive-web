from django.contrib.sitemaps import Sitemap
from .models import ArchiveProject, ArchiveService, ArchivePost, Page
from datetime import datetime


class ArchiveProjectSitemap(Sitemap):
    changeFreq = 'monthly'
    priority = 0.5


    def items(self):
        return ArchiveProject.objects.all()

    def lastmod(self, obj):
        return obj.project_updated_at

    def location(self, obj):
        return obj.get_absolute_url()


class ArchiveServiceSitemap(Sitemap):
    changeFreq = 'never'
    priority = 0.6


    def items(self):
        return ArchiveService.objects.all()

    def lastmod(self, obj):
        return obj.service_updated_at

    def location(self, obj):
        return obj.get_absolute_url()


class ArchiveBlogSitemap(Sitemap):
    changeFreq = 'weekly'
    priority = 0.5


    def items(self):
        return ArchivePost.objects.all()

    def lastmod(self, obj):
        return obj.post_updated_at

    def location(self, obj):
        return obj.get_absolute_url()


class PageSitemap(Sitemap):
    changeFreq = 'never'
    priority = 1.0


    def items(self):
        return Page.objects.all()

    def lastmod(self, obj):
        return obj.page_updated_at

    def location(self, obj):
        return obj.get_absolute_url()
