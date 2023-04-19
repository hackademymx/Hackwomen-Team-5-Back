from django.db import models
from places.models import Places
#from users.models import Users
# Create your models here.

class Comments(models.Model):

    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    comment = models.TextField ()
    created = models.DateTimeField(auto_now_add= True)




    
   
class Meta:
        db_table ='comments'
    
def _str_ (self):
        return self.comment
