from rest_framework.views import APIView
from .models import Post, Comment
from .serializers import PostModelSerializer, PostCreateSerializer, PostUpdateSerializer, CommentModelSerializer, CommentCreateSerializer, CommentUpdateSerializer
from rest_framework.response import Response
from rest_framework import status


class PostModelGetView(APIView):

    def get(self,request):
        posts = Post.objects.all()
        postserializer = PostModelSerializer(posts,many = True)
        return Response(postserializer.data, status.HTTP_200_OK)
    
    def put(self, request, pk,  *args, **kwargs):
        try:
           postt =  Post.objects.get(pk = pk)
        except Post.DoesNotExist:
            return Response({"Error":"Model not found "}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PostUpdateSerializer(postt, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Changed Successfully"},status=status.HTTP_201_CREATED)        
        return Response({"erros":"Error","detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk,  *args, **kwargs):
        try:
           postt =  Post.objects.get(pk = pk)
        except Post.DoesNotExist:
            return Response({"Error":"Model not found "}, status.HTTP_404_NOT_FOUND)
        
        postt.delete()
        return Response({"message":"Deleted"}, status.HTTP_200_OK)
        


class PostModelCreateView(APIView):

    def post(self,request,*args, **kwargs):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Created Successfully"},status=status.HTTP_201_CREATED)        
        return Response({"erros":"Error","detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


#--------------------------------------------
    
class CommentModelGetView(APIView):

    def get(self,request):
        comments = Comment.objects.all()
        commentserializer = CommentModelSerializer(comments,many = True)
        return Response(commentserializer.data, status.HTTP_200_OK)
    
    def put(self, request, pk,  *args, **kwargs):
        try:
           commentt =  Comment.objects.get(pk = pk)
        except Post.DoesNotExist:
            return Response({"Error":"Model not found "}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CommentUpdateSerializer(commentt, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Changed Successfully"},status=status.HTTP_201_CREATED)        
        return Response({"erros":"Error","detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk,  *args, **kwargs):
        try:
           commentt =  Comment.objects.get(pk = pk)
        except Comment.DoesNotExist:
            return Response({"Error":"Model not found "}, status.HTTP_404_NOT_FOUND)
        
        commentt.delete()
        return Response({"message":"Deleted"}, status.HTTP_200_OK)
        


class CommentModelCreateView(APIView):

    def post(self,request,*args, **kwargs):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Created Successfully"},status=status.HTTP_201_CREATED)        
        return Response({"erros":"Error","detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



