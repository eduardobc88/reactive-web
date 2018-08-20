from django.shortcuts import render
from .models import ArchiveProject, ArchiveService, ArchivePost, Page, SiteOption, HomeSlider
from django.views import generic


# Create your views here.


def home(request):
    home_slides = HomeSlider.objects.all()
    return render(
        request,
        'home.html',
        context = {
            'name': 'index',
            'home_slides': home_slides,
        }
    )


class PageDetailView(generic.DetailView):
    template_name = ''
    model = Page
    context_object_name = 'page'
    slug_field = 'page_slug'


    def get_context_data(self, **kwargs):
        self.template_name = self.object.page_template


class ArchiveProjectListView(generic.ListView):
    template_name = 'archive-project/project-list.html'
    model = ArchiveProject
    paginate_by = 10
    context_object_name = 'projects'


    def get_paginate_by(self, queryset):
        site_option = SiteOption.objects.filter(site_option_name='paginate_by')
        self.paginate_by = int(site_option.values('site_option_value')[0]['site_option_value'])
        return self.request.GET.get('paginate_by', self.paginate_by)


class ArchiveProjectDetailView(generic.DetailView):
    template_name = 'archive-project/project-detail.html'
    model = ArchiveProject
    context_object_name = 'project'
    slug_field = 'project_slug'


class ArchiveServiceListView(generic.ListView):
    template_name = 'archive-service/service-list.html'
    model = ArchiveService
    paginate_by = 10
    context_object_name = 'services'


    def get_paginate_by(self, queryset):
        # NOTE: the paginate_by property should to be created on admin site options section
        site_option = SiteOption.objects.filter(site_option_name='paginate_by')
        self.paginate_by = int(site_option.values('site_option_value')[0]['site_option_value'])
        return self.request.GET.get('paginate_by', self.paginate_by)


class ArchiveServiceDetailView(generic.DetailView):
    template_name = 'archive-service/service-detail.html'
    model = ArchiveService
    context_object_name = 'service'
    slug_field = 'service_slug'


class ArchivePostListView(generic.ListView):
    template_name = 'archive-blog/archive.html'
    model = ArchivePost
    paginate_by = 10
    context_object_name = 'posts'


    def get_paginate_by(self, queryset):
        site_option = SiteOption.objects.filter(site_option_name='paginate_by')
        self.paginate_by = int(site_option.values('site_option_value')[0]['site_option_value'])
        return self.request.GET.get('paginate_by', self.paginate_by)


class ArchivePostDetailView(generic.DetailView):
    template_name = 'archive-blog/single.html'
    model = ArchivePost
    context_object_name = 'post'
    slug_field = 'post_slug'
