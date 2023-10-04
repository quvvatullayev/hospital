from django.urls import path
from .views.hospital import HospitalListCreateView, HospitalRetrieveUpdateDestroyView

urlpatterns = [
    path('hospital/list/', HospitalListCreateView.as_view()),
    path('hospital/detil/<int:pk>/', HospitalRetrieveUpdateDestroyView.as_view())
]