from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer, ProductCreateSerializer, ProductSerializer, ProductUpdateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note, Product
from django.http import FileResponse, HttpResponse, HttpResponseNotFound
import os
from django.conf import settings
# Create your views here.
            
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() 
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    

# class LogoutView(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request):
#         logout(request)
#         return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [AllowAny]
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductCreateSerializer
        return ProductSerializer
    
class ProductListRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [AllowAny]
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ProductUpdateSerializer
        return ProductSerializer
        
def serve_image(request, image_name):
    # Construct the path to the image file
    image_path = os.path.join(settings.MEDIA_ROOT, 'product_images', image_name)
    
    # Check if the file exists
    if os.path.exists(image_path):
        # Open the file and read its content
        with open(image_path, 'rb') as f:
            image_data = f.read()
        # Return the image data as an HTTP response
        return HttpResponse(image_data, content_type='image/jpeg')
    else:
        # Return a 404 response if the file does not exist
        return HttpResponseNotFound()