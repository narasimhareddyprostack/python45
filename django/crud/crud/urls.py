
from django.contrib import admin
from django.urls import path
from userapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.gethomepage),
    path("add/", views.getnewuserpage),
    path("newemp/", views.getnewemppage),
]
