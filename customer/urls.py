from django.urls import path
from .views.customer import CustomerListCreateView, CustomerRetrieveUpdateDestroyView

urlpatterns = [
    # Customer views
    path('list/', CustomerListCreateView.as_view()),
    path('detil/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view()),
]