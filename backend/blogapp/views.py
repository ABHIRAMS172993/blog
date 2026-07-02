from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import BlogModel
from .serializers import BlogSerializer,RegisterSerializer,LoginSerializer
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.


@api_view(['GET'])
def view_blog(request):
    blogs = BlogModel.objects.all()
    serializer = BlogSerializer(blogs,many = True)
    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        # serializer.save(author=request.user)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])

def edit_blog(request,id):
    try:
        blog = BlogModel.objects.get(id=id)
    except BlogModel.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer = BlogSerializer(blog,data = request.data,partial =True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_blog(request,id):
    try:
        blog = BlogModel.objects.get(id=id)
    except BlogModel.DoesNotExist:
        return Response({'error':f"Blog with id {id} not found"})
    
    blog.delete()
    return redirect('/')

@api_view(['POST'])
@permission_classes([AllowAny])
def register_login(request):
    serializer = RegisterSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    serializer = LoginSerializer(data = request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username = username,password = password)
        if user is not None:
            return Response({"message":"you are logged in"},status=status.HTTP_200_OK)
        
        
    return Response({"error":"Your username and password is incorrect"},status = status.HTTP_401_UNAUTHORIZED)
        
def view_blog_user():
    pass





# {
#   "username": "AbhiramS",
#   "email": "abhi@gmail.com",
#   "password": "Abhi@12Chediroad"
# }