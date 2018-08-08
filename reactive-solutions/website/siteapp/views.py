from django.shortcuts import render
from .models import ArchiveProject, ArchiveService
from django.views import generic


# Create your views here.


def index(request):
    return render(
        request,
        'index.html',
        context = {
            'name': 'index'
        }
    )


class ArchiveProjectListView(generic.ListView):
    template_name = 'archive-project/project-list.html'
    model = ArchiveProject
    paginate_by = 2
    context_object_name = 'projects'


class ArchiveProjectDetailView(generic.DetailView):
    template_name = 'archive-project/project-detail.html'
    model = ArchiveProject
    context_object_name = 'project'
    slug_field = 'project_slug'


class ArchiveServiceListView(generic.ListView):
    template_name = 'archive-service/service-list.html'
    model = ArchiveService
    paginate_by = 2
    context_object_name = 'services'


class ArchiveServiceDetailView(generic.DetailView):
    template_name = 'archive-service/service-detail.html'
    model = ArchiveService
    context_object_name = 'service'
    slug_field = 'service_slug'
