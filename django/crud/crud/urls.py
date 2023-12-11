
from django.contrib import admin
from django.urls import path
from empapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("create/", views.createempview),
    path("read", views.displayempview),
    path('update/<id>', views.upateempview),
    path('delete/<id>', views.deletempview)
]
