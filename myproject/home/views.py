from django.shortcuts import render
from  django.http import HttpResponse
from . models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view
from . serializer import StudentSerializer
from rest_framework import status
def index(request):
    numbers={'num':[1,2,3,4,5,6,7,8,9]}
    return render(request,'index.html',numbers)
def about(request):
    return render(request,'about.html')
def contact(request):
    data={'student':Student.objects.all()}
    print(data)
    return render(request,'index.html',data)

@api_view(['GET'])

def index1(request):
    if request.method=='GET':
        student={
            "name":"abc",
            "place":"tcr"
        }
    return Response(student)

@api_view(['GET','POST'])
def index2(request):
    if request.method=='GET':
        queryset=Student.objects.all()
        serializer=StudentSerializer(queryset,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
@api_view(['GET','DELETE','PUT'])

def update(request,id):
    queryset=Student.objects.get(id=id)
    if request.method=='GET':
        serializer_class=StudentSerializer(queryset)
        return Response(serializer_class.data)
    elif request.method=='PUT':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method=='DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        

    







        


    
