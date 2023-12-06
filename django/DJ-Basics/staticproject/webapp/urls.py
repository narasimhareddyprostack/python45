from django.urls import path
from webapp import views
urlpatterns = [
    path('index/', views.getindex),
    path('about/', views.getabout),
    path('service/', views.getservice),
    path('contact/', views.getcontact),
]
