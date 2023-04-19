from django.urls import path
from .views import PlaceAPIView, PlaceAPIUpdateDeleteView


urlpatterns = [
    path('', PlaceAPIView.as_view(), name='places'),
    path('<int:id>/', PlaceAPIUpdateDeleteView.as_view(), name='place-update-delete'),
]
