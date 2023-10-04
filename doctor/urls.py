from django.urls import path
from .views.doctor import DoctorListCreateView, DoctorRetrieveUpdateDestroyView

urlpatterns = [
    path('doctor/list/', DoctorListCreateView.as_view()),
    path('doctor/detil/', DoctorRetrieveUpdateDestroyView.as_view())
]