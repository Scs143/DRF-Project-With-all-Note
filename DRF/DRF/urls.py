from django.contrib import admin
from django.urls import path, include
from DRFApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # Basic-----
    # path('drf/', views.DRFQuest_info),
    # path('drf/<int:pk>', views.DRFQuest_ins),
    
    # api_view or function based view-----
    # path('drfcreate/', views.DRFQuest_create),
    # path('drfcreate/<int:pk>', views.DRFQuest_create),
    
    # Class Based APIView----
    path('drfcreate/', views.DRFQuest_create.as_view()),
    path('drfcreate/<int:pk>/', views.DRFQuest_create.as_view()),
]
