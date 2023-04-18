from rest_framework.views import APIView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import Comments
from .serializers import CommentsSerializer
 


class CommentAPIView(APIView):
    def post(self, request):
        serializer = CommentsSerializer (data =request.data)
        serializer.is_valid (raise_exception= True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class CommentSingleView (APIView):

    def patch(self, request, pk):
        comment = Comments.objects.filter (pk=pk).first() #consulta a base de datos

        if comment is None:  #enviar respuesta en caso de que no se consiga
            return Response({'error':'Bad request.'}, status =status.HTTP_400_BAD_REQUEST)
        
        #si se encuentra se va a la base de datos y se actualiza
        serializer =CommentsSerializer(comment, data= request.data, partial=True )
        serializer.is_valid(raise_exception =True)
        serializer.save()
        return Response ('Comentario eliminado', status=status.HTTP_200_OK)
    

    def delete(self, request,pk):
        place = get_object_or_404 (Comments, pk=pk)
        place.delete()
        return Response('Comentario eliminado', status= status.HTTP_204_NO_CONTENT)
    
'''
class CommentAddLikeView(APIView):
    def post (self, request,pk):
        post = Comments.objects.get (pk=pk)
        
        is_dislike =False 

        for dislike in post.dislikes.all ():
            if dislike == request.user:
                is_dislike =True
                break 
        
        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like =True
                break

        if not is_like:
            post.likes.add(request.user)
        if is_like:
            post.likes.remove(request.user)

        
      #  next =request.POST.get('next','/')
        return Response()
    

    
class CommentAddDislike(APIView):
    def post (self, request,pk):
        post = Comments.objects.get (pk=pk)

        is_like =False 
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike =False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)
        if is_dislike:
            post.dislikes.remove(request.user)

      #  next =request.POST.get('next','/')
        return HTTPResponseRedirect(next)  


         
'''
