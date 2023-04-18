from django.db import models
from places.models import Places
#from users.models import Users
# Create your models here.

class Comments(models.Model):

    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    comment = models.TextField ()
    created = models.DateTimeField(auto_now_add= True)


'''
    likes = models.ManyToManyField(Users, blank=True, related_names= 'likes')
    dislikes = models.ManyToManyField(Users, blank=True, related_names= 'dislikes')
'''



    
    #security =models.CharField (max_length=32)
    #comment_description =models.CharField (max_length=256)
class Meta:
        db_table ='comments'
    
def _str_ (self):
        return self.comment
'''
def num_likes(self):
       return self.likes.all().count()

class Like (models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)

'''
