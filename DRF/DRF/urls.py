from django.contrib import admin
from django.urls import path, include
from DRFApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('drf/', views.DRFQuest_info),
    # path('drf/<int:pk>', views.DRFQuest_ins),
    path('drfcreate/', views.DRFQuest_create),
    path('drfcreate/<int:pk>', views.DRFQuest_create),
]
