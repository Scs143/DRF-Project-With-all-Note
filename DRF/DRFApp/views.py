from django.shortcuts import render
from .models import DRFQuest
from .serializers import DRFSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.
# DRFQuest
def DRFQuest_info(request):
    # complex data 
    drf = DRFQuest.objects.all()
    # Convert python dic it's mean native data 
    serializer = DRFSerializer(drf, many=True)
    # Jason render
    jason_render = JSONRenderer().render(serializer.data)
    # Json Sent to user 
    return HttpResponse(jason_render, content_type='application/json')



# Model Instance to see the model instance singly
def DRFQuest_ins(request, pk):
    # complex data 
    drf = DRFQuest.objects.get(id=pk)
    # Convert python dic it's mean native data 
    serializer = DRFSerializer(drf, many=False)
    # Jason render
    jason_render = JSONRenderer().render(serializer.data)
    # Json Sent to user 
    return HttpResponse(jason_render, content_type='application/json')