from django.urls import path
from .views import LikeDislikeCreateView, LikeDislikeDeleteView


urlpatterns = [
   
    path ('<int:pk>/', LikeDislikeCreateView.as_view(),),
    path ('<int:pk>/', LikeDislikeDeleteView.as_view(),),
    
]
