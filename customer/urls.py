from django.urls import path
from .views.customer import CustomerListCreateView, CustomerRetrieveUpdateDestroyView

urlpatterns = [
    # Customer views
    path('customer/list/', CustomerListCreateView.as_view()),
    path('customer/detil/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view()),
]