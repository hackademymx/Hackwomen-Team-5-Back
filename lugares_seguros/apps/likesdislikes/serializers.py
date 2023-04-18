from rest_framework import serializers
from .models import LikesDislikes

#class PlaceSerializer(serializers.ModelSerializer):
 #   likes = serializers.PrimaryKeyRelatedField(many=True, queryset =LikesDislikes.objects.filter(vote=1))
 #   dislikes = serializers.PrimaryKeyRelatedField(many=True, queryset =LikesDislikes.objects.filter(vote=-1))



class LikeDislikeSerializer (serializers.ModelSerializer):
   
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created =serializers.DateTimeField()


    class Meta:
        model = LikesDislikes
        fields = (
            'user',
            'created',
            'vote'
        
)
