from django.contrib import admin
from django.urls import path, include
from DRFApp import views

# Model View SET 
from rest_framework.routers import DefaultRouter
# Create router object 
router = DefaultRouter()
# Register
router.register('drfcrud', views.DRFQuest_Model_View_Set, basename='teacher')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    
    # <------------------------------Third Party app basic things---------------------------------------->
    # path('drf/', views.DRFQuest_info),
    # path('drf/<int:pk>', views.DRFQuest_ins),
    
    
    # <------------------------------api_view or function based view---------------------------------------->
    # path('drfcreate/', views.DRFQuest_create),
    # path('drfcreate/<int:pk>', views.DRFQuest_create),
    
    
    # <------------------------------Class Based APIView---------------------------------------->
    # path('drfcreate/', views.DRFQuest_create.as_view()),
    # path('drfcreate/<int:pk>/', views.DRFQuest_create.as_view()),
    

    # <------------------------------GenericAPIView---------------------------------------->
    # # ListModelMixin
    # path('drflist/', views.DRFQuest_ListView.as_view()),
    # # CreateModelMixin
    # path('drfcreate/', views.DRFQuest_CreateView.as_view()),
    # # RetrieveModelMixin
    # path('drfretrieve/<int:pk>/', views.DRFQuest_RetrieveView.as_view()),
    # # UpdateModelMixin
    # path('drfupdate/<int:pk>/', views.DRFQuest_UpdateView.as_view()),
    # # DestroyModelMixin
    # path('drfdelete/<int:pk>/', views.DRFQuest_DeleteView.as_view()),



    # # <------------------------------GenericAPIView CRUD---------------------------------------->
    # path('drfcrud/', views.DRFQuest_crud.as_view(), name='drfquest-list-create'),
    # path('drfcrud/<int:pk>/', views.DRFQuest_crud.as_view(), name='drfquest-detail'),


    # # <------------------------------ListCreateAPiView CRUD---------------------------------------->
    # path('drfcrud/', views.DRFQuest_List_Create.as_view(), name='drfquest-list-create'),
    # path('drfcrud/<int:pk>/', views.DRFQuest_Retrieve_Update_Destroy.as_view(), name='drfquest-detail'),



    # <------------------------------Model View Set CRUD---------------------------------------->
    path('', include(router.urls)),


]
