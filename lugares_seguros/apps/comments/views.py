from rest_framework.views import APIView
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
