from django.urls import path, include

from panel.views import HomeView

app_name = "panel"

urlpatterns = [
        path("", HomeView.as_view(), name="home"),
        path("blog-category/", include("panel.blog-category.urls")),
        path("blog-tag/", include("panel.blog-tag.urls")),
        path("slider/", include("panel.slider.urls")),
        path("project-category/", include("panel.project-category.urls"))
        ]
