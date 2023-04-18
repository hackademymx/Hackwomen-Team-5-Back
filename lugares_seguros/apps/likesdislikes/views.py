from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .models import LikesDislikes
from .serializers import LikeDislikeSerializer


# Create your views here.

class LikeDislikeCreateView(APIView):
    def post (self, request):
        serializer = LikeDislikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)



        user = request.user
        vote = serializer.validated_data['vote']

        try: 
            likedislike =LikesDislikes.objects.get(user =user)
            likedislike.vote = vote
            likedislike.save()

        except LikesDislikes.DoesNotExist:
            likedislike = LikesDislikes.objects.create(user=user, vote=vote)


        return Response (serializer.data, status=status.HTTP_201_CREATED)
    

class LikeDislikeDeleteView(APIView):
    serializer_class = LikeDislikeSerializer

    def delete(self, request):
        user = request.user
        likedislike = LikesDislikes.objects.get (user=user)
        likedislike.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)