from django.urls import path

from .views import SliderListView, SliderCreateView,SliderDeleteView,SliderUpdateView

urlpatterns = [
        path("", SliderListView.as_view(), name="slider-list"),
        path("create/", SliderCreateView.as_view(), name="slider-create"),
        path("delete/<pk>/", SliderDeleteView.as_view(), name="slider-delete"),
        path("update/<pk>/", SliderUpdateView.as_view(), name="slider-update"),

        ]