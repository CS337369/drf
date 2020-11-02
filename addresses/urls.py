from django.urls import path
from . import views

urlpatterns = [
    path('addresses/', views.address_list, name="addresses"),
    path('addresses/<int:pk>/', views.address, name="addresses-detail"),
    path('login/', views.login, name="login"),
    # path('', views.login_page, name="login_page")
]