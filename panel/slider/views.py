from django.views.generic import ListView
from common.models import Slider
from helpers.views import CreateView , DeleteView, UpdateView
from .forms import SliderForm


class SliderListView(ListView):
    model = Slider
    template_name = "panel/slider/list.html"
    context_object_name = "objects"
    queryset = model.objects.all().order_by("-id")
    paginate_by = 10

    def get_queryset(self):
        object_list = self.queryset
        search = self.request.GET.get("search", None)
        if search:
            object_list = object_list.filter(title__icontains=search)

        return object_list
    

class SliderCreateView(CreateView):
    model = Slider
    form_class = SliderForm
    template_name = "panel/slider/create.html"
    context_object_name = "object"
    success_url = "panel:slider-list"
    success_create_url = "panel:slider-create"



class SliderDeleteView(DeleteView):
    model = Slider
    success_url ="panel:slider-list"
    context_object_name = "object"
   



class SliderUpdateView(UpdateView):
    model = Slider
    form_class = SliderForm
    template_name = "panel/slider/create.html"
    context_object_name = "object"
    success_url = "panel:slider-list"
    success_create_url = "panel:slider-update"
