from django.contrib import admin
from django.urls import path
from userapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.getuserdata),
    path('', views.gethomepage),
]
