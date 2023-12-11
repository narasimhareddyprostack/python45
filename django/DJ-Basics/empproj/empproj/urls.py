
from django.contrib import admin
from django.urls import path
from empapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.gethomepage, name='home'),
    path('add/', views.getempregpage, name='reg'),
    path('saveemp/', views.getsuccesspage, name='saveemp'),
    path('saveuser/', views.getusersuccesspage, name='saveuser'),
    path('adduser/', views.getuserreg, name='userreg')
]
