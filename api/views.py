from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .seriallizers import Taskserializer 
from .models import Task 
# Create your views here.
@api_view(['GET'])
def apiOverview(request): 
    return Response("Up Man U!") 

@api_view(['GET'])
def taskList(request): 
    task = Task.objects.all() 
    serializer = Taskserializer(task, many=True) 
    return Response(serializer.data) 


@api_view(['GET'])
def taskDetail(request, pk): 
    task = Task.objects.get(id=pk) 
    serializer = Taskserializer(task, many=False) 
    return Response(serializer.data) 

@api_view(['POST']) 
def taskCreate(request): 
    serializer = Taskserializer(data=request.data) 
    if serializer.is_valid():
        serializer.save() 

    return Response(serializer.data)     

@api_view(['POST']) 
def taskUpdate(request, pk): 
    task = Task.objects.get(id=pk)
    serializer = Taskserializer(instance=task, data=request.data)  
    if serializer.is_valid():
        serializer.save() 

    return Response(serializer.data)     


@api_view(['DELETE']) 
def taskDelete(request, pk): 
    task = Task.objects.get(id=pk) 
    task.delete()     

    return Response("successfully deleted") 