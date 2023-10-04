from django.urls import path
from .views.doctor import DoctorListCreateView, DoctorRetrieveUpdateDestroyView
from .views.commit import CommintListCreateView, CommintRetrieveUpdateDestroyView

urlpatterns = [
    # Doctor viwes
    path('list/', DoctorListCreateView.as_view()),
    path('detil/', DoctorRetrieveUpdateDestroyView.as_view()),

    # Commint views
    path('commint/list/', CommintListCreateView.as_view()),
    path('commint/detil/', CommintRetrieveUpdateDestroyView.as_view()),
]