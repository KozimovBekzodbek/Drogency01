from django.urls import path

from .views import BlogCategoryListView, BlogCategoryCreateView, BlogCategoryDeleteView,BlogCategoryUpdateView

urlpatterns = [
        path("", BlogCategoryListView.as_view(), name="blog-category-list"),
        path("create/", BlogCategoryCreateView.as_view(), name="blog-category-create"),
        path("delete/<pk>/", BlogCategoryDeleteView.as_view(), name="blog-category-delete"),
        path("update/<pk>/", BlogCategoryUpdateView.as_view(), name="blog-category-update"),
        ]
