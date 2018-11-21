from django.contrib import admin
from django.conf import settings
from django.utils.safestring import mark_safe
from .models import ArchiveProject, HomeSlider, SiteOption, Banner, ArchiveService, ArchivePost, Page, Prospect

# Register your admin models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'admin_display_page_slug', 'page_template', 'thumbnail_preview', 'page_status', 'page_updated_at')
    readonly_fields = ['page_slug', 'page_created_at', 'page_updated_at']

    def thumbnail_preview(self, obj):
        image_url = 'https://placehold.it/1000x400/bfbfbf/fff/?text=RW'
        if obj.page_thumbnail:
            image_url = "{0}{1}".format(settings.MEDIA_URL, obj.page_thumbnail)
        return mark_safe('<img src="{0}" height="30"/>'.format(image_url))
    pass


@admin.register(ArchivePost)
class ArchivePostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'admin_display_post_slug', 'thumbnail_preview', 'post_status', 'post_updated_at')
    readonly_fields = ['post_slug', 'post_created_at', 'post_updated_at']

    def thumbnail_preview(self, obj):
        image_url = 'https://placehold.it/1000x400/bfbfbf/fff/?text=RW'
        if obj.post_thumbnail:
            image_url = "{0}{1}".format(settings.MEDIA_URL, obj.post_thumbnail)
        return mark_safe('<img src="{0}" height="30"/>'.format(image_url))
    pass


@admin.register(ArchiveService)
class ArchiveServiceAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'admin_display_service_slug', 'thumbnail_preview', 'service_status', 'service_updated_at')
    readonly_fields = ['service_slug', 'service_created_at', 'service_updated_at']

    def thumbnail_preview(self, obj):
        image_url = 'https://placehold.it/1000x400/bfbfbf/fff/?text=RW'
        if obj.service_thumbnail:
            image_url = "{0}{1}".format(settings.MEDIA_URL, obj.service_thumbnail)
        return mark_safe('<img src="{0}" height="30"/>'.format(image_url))
    pass


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('banner_name', 'admin_display_banner_content', 'thumbnail_preview')
    readonly_fields = ['thumbnail_preview']

    def thumbnail_preview(self, obj):
        image_url = 'https://placehold.it/350x350/bfbfbf/fff/?text=RW'
        if obj.banner_thumbnail:
            image_url = "{0}{1}".format(settings.MEDIA_URL, obj.banner_thumbnail)
        return mark_safe('<img src="{0}" height="30"/>'.format(image_url))
    pass


@admin.register(SiteOption)
class SiteOptionAdmin(admin.ModelAdmin):
    list_display = ('site_option_name', 'admin_display_site_option_value')
    pass


@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ('slide_title', 'slide_content', 'thumbnail_preview')
    readonly_fields = ['thumbnail_preview']

    def thumbnail_preview(self, obj):
        image_url = 'https://placehold.it/350x350/bfbfbf/fff/?text=RW'
        if obj.slide_image:
            image_url = "{0}{1}".format(settings.MEDIA_URL, obj.slide_image)
        return mark_safe('<img src="{0}" height="30"/>'.format(image_url))
    pass


@admin.register(ArchiveProject)
class ArchiveProjectAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'project_slug', 'thumbnail_preview', 'project_status', 'project_updated_at')
    readonly_fields = ['project_slug', 'thumbnail_preview', 'project_created_at', 'project_updated_at']

    def thumbnail_preview(self, obj):
        image_url = 'https://placehold.it/1000x400/bfbfbf/fff/?text=RW'
        if obj.project_thumbnail:
            image_url = "{0}{1}".format(settings.MEDIA_URL, obj.project_thumbnail)
        return mark_safe('<img src="{0}" height="30"/>'.format(image_url))
    pass


@admin.register(Prospect)
class ProspectAdmin(admin.ModelAdmin):
    list_display= ('prospect_name', 'prospect_email', 'prospect_phone', 'prospect_created_at', 'prospect_type')
    readonly_fields = ['prospect_name', 'prospect_last_name', 'prospect_email', 'prospect_phone', 'prospect_website', 'prospect_type', 'prospect_design_required', 'prospect_total_pages', 'prospect_message', 'prospect_created_at']
    pass
