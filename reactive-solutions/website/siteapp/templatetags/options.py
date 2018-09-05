from django import template
from ..models import Banner, SiteOption
register = template.Library()


@register.simple_tag
def who_we_are_slug():
    return '/quienes-somos/'

@register.simple_tag
def contact_slug():
    return '/contacto/'

@register.simple_tag
def privacy_slug():
    return '/aviso-de-privacidad/'

@register.simple_tag
def terms_conditions_slug():
    return '/terminos-y-condiciones/'

@register.simple_tag
def fb_url():
    return SiteOption.objects.filter(site_option_name='facebook_url').distinct().values_list('site_option_value', flat=True)[0]

@register.simple_tag
def tw_url():
    return SiteOption.objects.filter(site_option_name='twitter_url').distinct().values_list('site_option_value', flat=True)[0]

@register.simple_tag
def gp_url():
    return SiteOption.objects.filter(site_option_name='google_plus_url').distinct().values_list('site_option_value', flat=True)[0]

@register.simple_tag
def get_contact_banner_data():
    banner = Banner.objects.filter(banner_name='contact-banner').distinct()
    return {
        'banner_title': banner.values('banner_title')[0]['banner_title'],
        'banner_content': banner.values('banner_content')[0]['banner_content'],
        'banner_thumbnail': banner.values('banner_thumbnail')[0]['banner_thumbnail'],
        'banner_button_name': banner.values('banner_button_name')[0]['banner_button_name'],
        'banner_button_url': banner.values('banner_button_url')[0]['banner_button_url'],
    }

@register.simple_tag
def get_who_banner_data():
    banner = Banner.objects.filter(banner_name='who-banner').distinct()
    return {
        'banner_title': banner.values('banner_title')[0]['banner_title'],
        'banner_content': banner.values('banner_content')[0]['banner_content'],
        'banner_thumbnail': banner.values('banner_thumbnail')[0]['banner_thumbnail'],
        'banner_button_name': banner.values('banner_button_name')[0]['banner_button_name'],
        'banner_button_url': banner.values('banner_button_url')[0]['banner_button_url'],
    }

@register.simple_tag
def get_services_description():
    return SiteOption.objects.filter(site_option_name='services_description').distinct().values_list('site_option_value', flat=True)[0]

@register.simple_tag
def get_projects_description():
    return SiteOption.objects.filter(site_option_name='projects_description').distinct().values_list('site_option_value', flat=True)[0]

@register.simple_tag
def get_blog_description():
    return SiteOption.objects.filter(site_option_name='blog_description').distinct().values_list('site_option_value', flat=True)[0]
