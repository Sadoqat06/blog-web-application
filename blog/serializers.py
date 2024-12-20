from rest_framework import serializers
from .models import  Post, Comment



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserModel
#         fields = ['name','surname']


class PostModelSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Post
        fields = ['author','title','content', 'created_at', 'updated_at']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content','created_at', 'updated-at']

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content','created_at', 'updated-at']

#_________________________________________________

class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post','author_name', 'content', 'created_at']  

    
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'content', 'created_at']


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'content', 'created_at']