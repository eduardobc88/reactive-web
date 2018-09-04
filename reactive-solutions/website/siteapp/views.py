from django.shortcuts import render
from .models import ArchiveProject, ArchiveService, ArchivePost, Page, SiteOption, HomeSlider, Prospect
from django.views import generic
from django.http import HttpResponseRedirect
from django.conf import settings


# Create your views here.


def home(request):
    slides = HomeSlider.objects.all()
    posts = ArchivePost.objects.all().order_by('-id')[:3]
    projects = ArchiveProject.objects.all().order_by('-id')[:3]
    services = ArchiveService.objects.all().order_by('-id')

    return render(
        request,
        'home.html',
        context = {
            'slides': slides,
            'posts': posts,
            'projects': projects,
            'services': services,
            'page_head_title': 'REACTIVE WEB',
            'page_head_description': 'REACTIVE WEB: Desarrollo y Diseño Web',
            'page_head_bar_color': '#24a9e1',
        }
    )

def thanks(request):
    page = Page.objects.filter(page_slug='gracias')
    page_data = {
        'page_title':page.values('page_title')[0]['page_title'],
        'page_content':page.values('page_content')[0]['page_content'],
        'page_thumbnail':page.values('page_thumbnail')[0]['page_thumbnail'],
        }
    page_head_title = page.values_list('page_title', flat=True)[0]
    page_head_description = page.values_list('page_excerpt', flat=True)[0]

    if request.POST:
        prospect = Prospect(
            prospect_name = request.POST.get('contact_name', ''),
            prospect_last_name = request.POST.get('contact_lastname', ''),
            prospect_email = request.POST.get('contact_email', ''),
            prospect_phone = request.POST.get('contact_phone', ''),
            prospect_website = request.POST.get('contact_website', ''),
            prospect_message = request.POST.get('contact_message', ''),
            )
        prospect.save()
        page_slug = page.values('page_slug')[0]['page_slug']
        return HttpResponseRedirect('/{0}/'.format(page_slug))

    return render(
        request,
        page.values('page_template')[0]['page_template'],
        context = {
            'page': page_data,
            'page_head_title': 'RW - {0}'.format(page_head_title),
            'page_head_description': page_head_description,
            'page_head_bar_color': '#24a9e1',
        }
    )


class PageDetailView(generic.DetailView):
    template_name = ''
    model = Page
    context_object_name = 'page'
    slug_field = 'page_slug'


    def get_queryset(self):
        self.model = Page.objects.filter(page_slug=self.kwargs.get('slug'))
        return self.model

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.template_name = self.object.page_template
        context['page_head_title'] = 'RW - {0}'.format(self.object.page_title)
        context['page_head_description'] = self.object.page_excerpt
        context['page_head_bar_color'] = '#24a9e1'
        return context


class ArchiveProjectListView(generic.ListView):
    template_name = 'archive-project/archive.html'
    model = ArchiveProject
    paginate_by = 10
    context_object_name = 'projects'


    def get_paginate_by(self, queryset):
        site_option = SiteOption.objects.filter(site_option_name='paginate_by')
        self.paginate_by = int(site_option.values('site_option_value')[0]['site_option_value'])
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_head_title'] = 'RW - Proyectos'
        context['page_head_description'] = 'Proyectos que hemos realizado.',
        context['page_head_bar_color'] = '#24a9e1'
        return context


class ArchiveProjectDetailView(generic.DetailView):
    template_name = 'archive-project/single.html'
    model = ArchiveProject
    context_object_name = 'project'
    slug_field = 'project_slug'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_head_title'] = 'RW - {0}'.format(self.object.project_title)
        context['page_head_description'] = self.object.project_excerpt
        context['page_head_bar_color'] = '#24a9e1'
        return context


class ArchiveServiceListView(generic.ListView):
    template_name = 'archive-service/archive.html'
    model = ArchiveService
    paginate_by = 10
    context_object_name = 'services'


    def get_paginate_by(self, queryset):
        # NOTE: the paginate_by property should to be created on admin site options section
        site_option = SiteOption.objects.filter(site_option_name='paginate_by')
        self.paginate_by = int(site_option.values('site_option_value')[0]['site_option_value'])
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_head_title'] = 'RW - Services'
        context['page_head_description'] = 'Nuestros servicios'
        context['page_head_bar_color'] = '#24a9e1'
        return context


class ArchiveServiceDetailView(generic.DetailView):
    template_name = 'archive-service/single.html'
    model = ArchiveService
    context_object_name = 'service'
    slug_field = 'service_slug'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_head_title'] = 'RW - {0}'.format(self.object.service_title)
        context['page_head_description'] = self.object.service_excerpt
        context['page_head_bar_color'] = '#24a9e1'
        return context


class ArchivePostListView(generic.ListView):
    template_name = 'archive-blog/archive.html'
    model = ArchivePost
    paginate_by = 10
    context_object_name = 'posts'


    def get_paginate_by(self, queryset):
        site_option = SiteOption.objects.filter(site_option_name='paginate_by')
        self.paginate_by = int(site_option.values('site_option_value')[0]['site_option_value'])
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_head_title'] = 'RW - Blog'
        context['page_head_description'] = 'En nuestro blog podras encontrar desde noticias relevantes hasta tutoriales de desarrollo web.'
        context['page_head_bar_color'] = '#24a9e1'
        return context


class ArchivePostDetailView(generic.DetailView):
    template_name = 'archive-blog/single.html'
    model = ArchivePost
    context_object_name = 'post'
    slug_field = 'post_slug'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_head_title'] = 'RW - {0}'.format(self.object.post_title)
        context['page_head_description'] = self.object.post_excerpt
        context['page_head_bar_color'] = '#24a9e1'
        return context
