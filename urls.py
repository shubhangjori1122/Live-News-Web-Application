
from django.contrib import admin
from django.urls import path
from nwapp.views import home,about

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",home,name="home"),
    path("about",about,name="about"),
]


handler404= "nwapp.views.pnf"
