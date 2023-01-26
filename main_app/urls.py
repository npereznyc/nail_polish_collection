from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('brands/', views.BrandList.as_view(), name='brand_list'),
    path('polishes/', views.PolishList.as_view(), name='polish_list'),
    path('polishes/new/', views.PolishCreate.as_view(), name='polish_create'),
    # path('brands/<int:pk>/', views.BrandPolishes.as_view(), name='brand_polishes'),
    path('polishes/<int:pk>/', views.PolishDetail.as_view(), name='polish_detail'),
    path('polishes/<int:pk>', views.PolishUpdate.as_view(), name='polish_update'),
    path('polishes/<int:pk>/delete', views.PolishDelete.as_view(), name='polish_delete')
]