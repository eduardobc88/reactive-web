from django.shortcuts import render
from .models import ArchiveProject, ArchiveService, ArchivePost, Page, SiteOption, HomeSlider, Prospect
from django.views import generic
from django.http import HttpResponseRedirect
from django.conf import settings


# Create your views here.

def get_site_option_value(option_name):
    site_options = SiteOption.objects.all()
    option = site_options.filter(site_option_name=option_name)
    if not option:
        return False
    return option.values_list('site_option_value', flat=True).distinct()[0]


def home(request):
    slides = HomeSlider.objects.all().order_by('-id')
    posts = ArchivePost.objects.all().order_by('-id')[:3]
    projects = ArchiveProject.objects.all().order_by('-id')[:3]
    services = ArchiveService.objects.all().order_by('-id')
    website_head_title = get_site_option_value('page_head_title')
    page_head_description = get_site_option_value('page_home_head_description')

    return render(
        request,
        'home.html',
        context = {
            'slides': slides,
            'posts': posts,
            'projects': projects,
            'services': services,
            'page_head_title': website_head_title,
            'page_head_description': page_head_description,
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
    website_head_title = get_site_option_value('page_head_title')
    page_title = page.values_list('page_title', flat=True)[0]
    page_excerpt = page.values_list('page_excerpt', flat=True)[0]

    if request.POST:
        prospect = Prospect(
            prospect_name = request.POST.get('contact_name', ''),
            prospect_last_name = request.POST.get('contact_lastname', ''),
            prospect_email = request.POST.get('contact_email', ''),
            prospect_phone = request.POST.get('contact_phone', ''),
            prospect_website = request.POST.get('contact_website', ''),
            prospect_message = request.POST.get('contact_message', ''),
            prospect_type = request.POST.get('contact_type', ''),
            prospect_total_pages = request.POST.get('contact_total_pages', ''),
            prospect_design_required = request.POST.get('contact_design_required', ''),
            )
        prospect.save()
        page_slug = page.values('page_slug')[0]['page_slug']
        return HttpResponseRedirect('/{0}/'.format(page_slug))

    return render(
        request,
        page.values('page_template')[0]['page_template'],
        context = {
            'page': page_data,
            'page_head_title': '{0} - {1}'.format(website_head_title, page_title),
            'page_head_description': page_excerpt,
            'page_head_bar_color': '#24a9e1',
        }
    )


class PageDetailView(generic.DetailView):
    template_name = ''
    model = Page
    context_object_name = 'page'
    slug_field = 'page_slug'
    website_head_title = get_site_option_value('page_head_title')


    def get_queryset(self):
        self.model = Page.objects.filter(page_slug=self.kwargs.get('slug'), page_status='publish')
        return self.model

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.template_name = self.object.page_template
        context['page_head_title'] = '{0} - {1}'.format(self.website_head_title, self.object.page_title)
        context['page_head_description'] = self.object.page_excerpt
        context['page_head_bar_color'] = '#24a9e1'
        return context


class ArchiveProjectListView(generic.ListView):
    template_name = 'archive-project/archive.html'
    model = ArchiveProject
    paginate_by = 10
    context_object_name = 'projects'
    website_head_title = get_site_option_value('page_head_title')


    def get_paginate_by(self, queryset):
        self.paginate_by = int(get_site_option_value('paginate_by'))
        return self.paginate_by

    def get_queryset(self):
        return self.model.objects.filter(project_status='publish')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects_title = get_site_option_value('projects_title')
        projects_description = get_site_option_value('projects_description')
        context['page_head_title'] = '{0} - {1}'.format(self.website_head_title, projects_title)
        context['page_head_description'] = projects_description
        context['page_head_bar_color'] = '#24a9e1'
        return context


class ArchiveProjectDetailView(generic.DetailView):
    template_name = 'archive-project/single.html'
    model = ArchiveProject
    context_object_name = 'project'
    slug_field = 'project_slug'
    website_head_title = get_site_option_value('page_head_title')


    def get_queryset(self):
        return self.model.objects.filter(project_status='publish')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_head_title'] = '{0} - {1}'.format(self.website_head_title, self.object.project_title)
        context['page_head_description'] = self.object.project_excerpt
        context['page_head_bar_color'] = '#24a9e1'
        return context


class ArchiveServiceListView(generic.ListView):
    template_name = 'archive-service/archive.html'
    model = ArchiveService
    paginate_by = 10
    context_object_name = 'services'
    website_head_title = get_site_option_value('page_head_title')


    def get_paginate_by(self, queryset):
        self.paginate_by = int(get_site_option_value('paginate_by'))
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        return self.model.objects.filter(service_status='publish')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services_title = get_site_option_value('services_title')
        services_description = get_site_option_value('services_description')
        context['page_head_title'] = '{0} - {1}'.format(self.website_head_title, services_title)
        context['page_head_description'] = services_description
        context['page_head_bar_color'] = '#24a9e1'
        return context


class ArchiveServiceDetailView(generic.DetailView):
    template_name = 'archive-service/single.html'
    model = ArchiveService
    context_object_name = 'service'
    slug_field = 'service_slug'
    website_head_title = get_site_option_value('page_head_title')


    def get_queryset(self):
        return self.model.objects.filter(service_status='publish')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_head_title'] = '{0} - {1}'.format(self.website_head_title, self.object.service_title)
        context['page_head_description'] = self.object.service_excerpt
        context['page_head_bar_color'] = '#24a9e1'
        return context


class ArchivePostListView(generic.ListView):
    template_name = 'archive-blog/archive.html'
    model = ArchivePost
    paginate_by = 10
    context_object_name = 'posts'
    website_head_title = get_site_option_value('page_head_title')


    def get_paginate_by(self, queryset):
        self.paginate_by = int(get_site_option_value('paginate_by'))
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        return self.model.objects.filter(post_status='publish')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_title = get_site_option_value('blog_title')
        blog_description = get_site_option_value('blog_description')
        context['page_head_title'] = '{0} - {1}'.format(self.website_head_title, blog_title)
        context['page_head_description'] = blog_description
        context['page_head_bar_color'] = '#24a9e1'
        return context


class ArchivePostDetailView(generic.DetailView):
    template_name = 'archive-blog/single.html'
    model = ArchivePost
    context_object_name = 'post'
    slug_field = 'post_slug'
    website_head_title = get_site_option_value('page_head_title')


    def get_queryset(self):
        return self.model.objects.filter(post_status='publish')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_head_title'] = '{0} - {1}'.format(self.website_head_title, self.object.post_title)
        context['page_head_description'] = self.object.post_excerpt
        context['page_head_bar_color'] = '#24a9e1'
        return context
