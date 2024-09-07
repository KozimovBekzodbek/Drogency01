from django.urls import path

from .views import BlogTagListView,BlogTagCreateView,BlogTagDeleteView,BlogTagUpdateView

urlpatterns = [
        path("", BlogTagListView.as_view(), name="blog-tag-list"),
        path("create/", BlogTagCreateView.as_view(), name="blog-tag-create"),
        path("delete/<pk>/", BlogTagDeleteView.as_view(), name="blog-tag-delete"),
        path("update/<pk>/", BlogTagUpdateView.as_view(), name="blog-tag-update"),
          ]