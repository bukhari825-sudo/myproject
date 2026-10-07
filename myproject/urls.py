from django.contrib import admin
from django.urls import path
from myapp import views  # Isse views.home aur views.result dono kaam karenge

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
]