from django.shortcuts import render
from .models import ArchiveProject, ArchiveService, ArchivePost, Page, SiteOption, HomeSlider, Prospect
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

def thanks(request):
    prospect = Prospect(
        prospect_name = request.POST.get('contact_name', ''),
        prospect_last_name = request.POST.get('contact_lastname', ''),
        prospect_email = request.POST.get('contact_email', ''),
        prospect_phone = request.POST.get('contact_phone', ''),
        prospect_website = request.POST.get('contact_website', ''),
        prospect_message = request.POST.get('contact_message', ''),
        )
    prospect.save()

    return render(
        request,
        'page-template/default.html',
        context = {
            'page_title': 'Gracias por tu mensaje!',
            'page_content': 'Pronto nos pondremos en contácto.',
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


class ArchiveProjectDetailView(generic.DetailView):
    template_name = 'archive-project/single.html'
    model = ArchiveProject
    context_object_name = 'project'
    slug_field = 'project_slug'


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


class ArchiveServiceDetailView(generic.DetailView):
    template_name = 'archive-service/single.html'
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
