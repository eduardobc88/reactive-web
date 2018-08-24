from django import template
from ..models import Banner
register = template.Library()


# from ..models import YourModel


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
    return '#'

@register.simple_tag
def tw_url():
    return '#'

@register.simple_tag
def gp_url():
    return '#'

@register.simple_tag
def get_contact_banner_data():
    banner = Banner.objects.filter(banner_name='contact-banner')
    return {
        'banner_title': banner.values('banner_title')[0]['banner_title'],
        'banner_content': banner.values('banner_content')[0]['banner_content'],
        'banner_thumbnail': banner.values('banner_thumbnail')[0]['banner_thumbnail'],
        'banner_button_name': banner.values('banner_button_name')[0]['banner_button_name'],
        'banner_button_url': banner.values('banner_button_url')[0]['banner_button_url'],
    }

@register.simple_tag
def get_who_banner_data():
    banner = Banner.objects.filter(banner_name='who-banner')
    return {
        'banner_title': banner.values('banner_title')[0]['banner_title'],
        'banner_content': banner.values('banner_content')[0]['banner_content'],
        'banner_thumbnail': banner.values('banner_thumbnail')[0]['banner_thumbnail'],
        'banner_button_name': banner.values('banner_button_name')[0]['banner_button_name'],
        'banner_button_url': banner.values('banner_button_url')[0]['banner_button_url'],
    }
