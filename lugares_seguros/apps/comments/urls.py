from django.urls import path
from .views import CommentAPIView, CommentSingleView #CommentAddDislike, CommentAddLikeView

urlpatterns = [
    path ('', CommentAPIView.as_view(),),
    path ('<int:pk>/', CommentSingleView.as_view()),

    #path ('<int:pk>/like', CommentAddLikeView.as_view(), name= 'like'),
    #path ('<int:pk>/dislike', CommentAddDislike.as_view(), name ='dislike'),
]
