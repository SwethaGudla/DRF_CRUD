from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import TaskSerializers
from .models import Task
from rest_framework import status
from django.core.paginator import Paginator
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
# from django.http import JsonResponse
# Create your views here.
class Authenti(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        content = {'message':'welocme to our company'}
        return Response(content)
    
@api_view(['GET'])
def api_crud(request):
    return Response("API Base Point")


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def taskList(request):
    task = Task.objects.all()
    serializers = TaskSerializers(task, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def taskDetails(request,pk):
    task = Task.objects.get(id=pk)
    serializers = TaskSerializers(task,many=False)
    return Response(serializers.data)

@api_view(['POST'])
def taskCreate(request):
    # res = {}
    # if len(request.data.get("name"))<=2:
    #     message="Name should be more than 2 characters..!"
    #     res['name'] = [message]
    # if request.data.get("age")<=18:
    #     message="please enter age is greaterthan 18"
    #     res['age'] = [message]
    # if res:
    #     return Response(res)
    serializers = TaskSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED) 
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializers = TaskSerializers(instance = task,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item successfully deeleted..!")
