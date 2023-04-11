from django.urls import path
from .views import CommentAPIView, CommentSingleView

urlpatterns = [
    path ('', CommentAPIView.as_view(),),
    path ('<int:pk>/', CommentSingleView.as_view()),

]