
from django.urls import path

from .views import ProjectCategoryListView,ProjectCategoryCreateView,ProjectCategoryDeleteView,ProjectCategoryUpdateView

urlpatterns = [
        path("", ProjectCategoryListView.as_view(), name="project-category-list"),
        path("create/", ProjectCategoryCreateView.as_view(), name="project-category-create"),
        path("delete/<pk>/", ProjectCategoryDeleteView.as_view(), name="project-category-delete"),
        path("update/<pk>/", ProjectCategoryUpdateView.as_view(), name="project-category-update"),
          ]