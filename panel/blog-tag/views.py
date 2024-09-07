from django.views.generic import ListView

from common.models import BlogTag
from helpers.views import CreateView, UpdateView, DeleteView

from .forms import BlogTagForm


class BlogTagListView(ListView):
    model = BlogTag
    template_name = "panel/blog-tag/list.html"
    context_object_name = "objects"
    queryset = model.objects.all().order_by("-id")
    paginate_by = 10

    def get_queryset(self):
        object_list = self.queryset
        search = self.request.GET.get("search", None)
        if search:
            object_list = object_list.filter(title__icontains=search)

        return object_list
 

class BlogTagCreateView(CreateView):
    model = BlogTag
    form_class = BlogTagForm
    template_name = "panel/blog-tag/create.html"
    context_object_name = "object"
    success_url = "panel:blog-tag-list"
    success_create_url = "panel:blog-tag-create"


class BlogTagDeleteView(DeleteView):
    model = BlogTag
    success_url ="panel:blog-tag-list"
    context_object_name = "object"
    template_name = "panel/blog-tag/delete.html"



class BlogTagUpdateView(UpdateView):
    model = BlogTag
    form_class = BlogTagForm
    success_url ="panel:blog-tag-list"
    context_object_name = "object"
    template_name = "panel/blog-tag/update.html"
    success_create_url = "panel:blog-tag-update"
