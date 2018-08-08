from django.shortcuts import render
from .models import ArchiveProject
from django.views import generic
from django.shortcuts import get_object_or_404


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
    model = ArchiveProject
    # paginate_by = 2
    context_object_name = 'projects'


class ArchiveProjectDetailView(generic.DetailView):
    template_name = 'siteapp/archiveproject_detail.html'
    model = ArchiveProject
    context_object_name = 'project'
    slug_field = 'project_slug'
