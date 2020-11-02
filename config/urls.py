from django.contrib import admin
from django.urls import path, include
import addresses

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('addresses.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
