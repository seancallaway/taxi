from django.urls import path

from trips.views import TripView

app_name = 'trips'

urlpatterns = [
    path('', TripView.as_view({'get': 'list'}), name='list'),
    path('<uuid:pk>/', TripView.as_view({'get': 'retrieve'}), name='detail'),
]
