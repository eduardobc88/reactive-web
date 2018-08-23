from django.contrib import admin
from .models import ArchiveProject, HomeSlider, SiteOption, Banner, ArchiveService, ArchivePost, Page, Prospect


# Register your models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'admin_display_page_slug', 'page_template')
    readonly_fields = ['page_slug']
    pass


@admin.register(ArchivePost)
class ArchivePostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'admin_display_post_slug')
    readonly_fields = ['post_slug']
    pass


@admin.register(ArchiveService)
class ArchiveServiceAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'admin_display_service_slug')
    readonly_fields = ['service_slug']
    pass


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('banner_name', 'admin_display_banner_content')
    pass


@admin.register(SiteOption)
class SiteOptionAdmin(admin.ModelAdmin):
    list_display = ('site_option_name', 'admin_display_site_option_value')
    pass


@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ('slide_title', 'slide_content')
    pass


@admin.register(ArchiveProject)
class ArchiveProjectAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'project_slug')
    readonly_fields = ['project_slug']
    pass


@admin.register(Prospect)
class ProspectAdmin(admin.ModelAdmin):
    list_display= ('prospect_name', 'prospect_email', 'prospect_phone')
    readonly_fields = ['prospect_name', 'prospect_last_name', 'prospect_email', 'prospect_phone', 'prospect_website', 'prospect_message']
    pass
