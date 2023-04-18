from django.db import models
from users.models import Users
#from places.models import  Places
# Create your models here.

class LikesDislikes(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
   # place = models.ForeignKey(Places, on_delete=models.CASCADE)
    vote = models.IntegerField()
    
 
    
class Meta:
    db_table = 'likes_dislikes'

def _str_(self):
        return self.vote
