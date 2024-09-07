from django.views.generic import ListView

from common.models import ProjectCategory
from helpers.views import CreateView , DeleteView, UpdateView

from .forms import ProjectCategoryForm



class ProjectCategoryListView(ListView):
    model = ProjectCategory
    template_name = "panel/project-category/list.html"
    context_object_name = "objects"
    queryset = model.objects.all().order_by("-id")
    paginate_by = 10

    def get_queryset(self):
        object_list = self.queryset
        search = self.request.GET.get("search", None)
        if search:
            object_list = object_list.filter(title__icontains=search)

        return object_list


class ProjectCategoryCreateView(CreateView):
    model = ProjectCategory
    form_class = ProjectCategoryForm
    template_name = "panel/project-category/create.html"
    context_object_name = "object"
    success_url = "panel:project-category-list"
    success_create_url = "panel:project-category-create"


class ProjectCategoryDeleteView(DeleteView):

    model = ProjectCategory
    success_url ="panel:project-category-list"
    context_object_name = "object"
    



class ProjectCategoryUpdateView(UpdateView):
    model = ProjectCategory
    form_class = ProjectCategoryForm
    success_url ="panel:project-category-list"
    context_object_name = "object"
    success_create_url = "panel:project-category-update"