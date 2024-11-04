from django.shortcuts import render
from .models import DRFQuest
from .serializers import DRFSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response


# # Create your views here.
# api_view or function based view
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@csrf_exempt
def DRFQuest_create(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            #Complex data
            drf = DRFQuest.objects.get(id=id)
            # Convert into Python Dic 
            serializer = DRFSerializer(drf)
            return Response(serializer.data)
        # Complex data 
        drf = DRFQuest.objects.all()
        # Python Dic 
        serializer = DRFSerializer(drf, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        jason_data = request.data # Parse data
        serializer = DRFSerializer(data=jason_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Has Been Created SuccessFully'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = pk
        drf = DRFQuest.objects.get(id=id)
        serializer = DRFSerializer(drf, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Full Data has been Updated SuccessFully'})
        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        id = pk
        drf = DRFQuest.objects.get(id=id)
        serializer = DRFSerializer(drf, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data has been Updated SuccessFully'})
        return Response(serializer.errors)


    if request.method == 'DELETE':
        id = pk
        drf = DRFQuest.objects.get(id=id)
        drf.delete()
        return Response({'msg': 'ID Data has been Deleted SuccessFully'})





# # This is just test perpouse run by Third Party app basic things
# # Create your views here.
# # DRFQuest
# def DRFQuest_info(request):
#     # complex data 
#     drf = DRFQuest.objects.all()
#     # Convert python dic it's mean native data 
#     serializer = DRFSerializer(drf, many=True)
#     # Jason render
#     jason_render = JSONRenderer().render(serializer.data)
#     # Json Sent to user 
#     return HttpResponse(jason_render, content_type='application/json')



# # Model Instance to see the model instance singly
# def DRFQuest_ins(request, pk):
#     # complex data 
#     drf = DRFQuest.objects.get(id=pk)
#     # Convert python dic it's mean native data 
#     serializer = DRFSerializer(drf)
#     # Jason render
#     jason_render = JSONRenderer().render(serializer.data)
#     # Json Sent to user 
#     return HttpResponse(jason_render, content_type='application/json')


# @csrf_exempt
# def DRFQuest_create(request):
#     # Create
#     if request.method == 'POST':
#         jason_data = request.body
#         # json to stream convert
#         stream = io.BytesIO(jason_data)
#         # Stream to python data
#         python_data = JSONParser().parse(stream)
#         # python to complex data
#         serializer = DRFSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Created SuccessFully'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
        
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
#     # Update 
#     if request.method == 'PUT':
#         jason_data = request.body
#         # json to stream convert
#         stream = io.BytesIO(jason_data)
#         # Stream to python data
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         drf = DRFQuest.objects.get(id=id)
#         # python to complex data
#         serializer = DRFSerializer(drf, data=python_data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Updated SuccessFully'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')

#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type='application/json')
    
#     # Delete
#     if request.method == 'DELETE':
#         jason_data = request.body
#         # json to stream convert
#         stream = io.BytesIO(jason_data)
#         # Stream to python data
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id')
#         drf = DRFQuest.objects.get(id=id)
#         drf.delete()
#         res = {'msg': 'Data Deleted SuccessFully'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')