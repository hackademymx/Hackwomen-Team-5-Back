from django.urls import path
from .views import PlaceAPIView, PlaceAPIUpdateDeleteView


urlpatterns = [
    path('places/', PlaceAPIView.as_view(), name='places'),
    path('places/<int:id>/', PlaceAPIUpdateDeleteView.as_view(), name='place-update-delete'),
]