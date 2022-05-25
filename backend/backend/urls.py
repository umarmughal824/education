from contrib.views import char_count
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("char_count", char_count, name="char_count"),
    path("", include("quizes.urls"), name="quizes"),
    re_path(".*", TemplateView.as_view(template_name="index.html")),
]
