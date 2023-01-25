from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('brands/', views.BrandList.as_view(), name='brand_list'),
    path('polishes/', views.PolishList.as_view(), name='polish_list'),
]