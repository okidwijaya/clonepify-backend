from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note, Collection, Vendor, Product, Blog, Blogpost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}

class CollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "collection"]
        
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ["id", "vendor"]
        
class ProductSerializer(serializers.ModelSerializer):
    collection = serializers.CharField(max_length=100)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'collection', 'vendor', 'image', 'created_at', 'updated_at', 'tags', 'status', 'stock', 'compare_at_price', 'margin', 'profit', 'cost', 'variant']
        
    def create(self, validated_data):
        collection_name = validated_data.pop('collection', None)
        vendor_name = validated_data.pop('vendor', None)
        
        if collection_name:
            collection, _ = Collection.objects.get_or_create(collection=collection_name)
            validated_data['collection'] = collection
        
        if vendor_name:
            vendor, _ = Vendor.objects.get_or_create(vendor=vendor_name)
            validated_data['vendor'] = vendor
        
        return Blogpost.objects.create(**validated_data)
        
class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['id', 'created_at', 'updated_at']
        
    def validate_collection(self, value):
        if Collection.objects.filter(collection=value).exists():
            raise serializers.ValidationError('Collection already exists')
        return value
    
    def validate_vendor(self, value):
        if Vendor.objects.filter(vendor=value).exists():
            raise serializers.ValidationError('Vendor already exists')
        return value

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'collection', 'vendor', 'image', 'tags', 'status', 'stock', 'compare_at_price', 'margin', 'profit', 'cost', 'variant']
        
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'blog']
        
class BlogPostSerializer(serializers.ModelSerializer):
    blog = serializers.CharField(max_length=150)
    class Meta:
        model = Blogpost
        fields = ['id', 'title', 'content', 'created_at', 'author', 'tags', 'image', 'blog']
        
    def create(self, validated_data):
        blog_name = validated_data.pop('blog', None)
        
        if blog_name:
            blog, _ = Blog.objects.get_or_create(blog=blog_name)
            validated_data['blog'] = blog
        
        return Blogpost.objects.create(**validated_data)
    

class BlogPostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = ['title', 'content', 'author', 'tags', 'image', 'blog']
    
class BlogpostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        exclude = ['id', 'created_at']
        
    def validate_blogpost(self, value):
        if Blogpost.objects.filter(blog=value).exists():
            raise serializers.ValidationError('Blog already exists')
        return value
        