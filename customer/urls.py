from django.urls import path
from .views.customer import CustomerListCreateView, CustomerRetrieveUpdateDestroyView
from .views.order import OrderListCreateView, OrderRetrieveUpdateDestroyView

urlpatterns = [
    # Customer views
    path('list/', CustomerListCreateView.as_view()),
    path('detil/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view()),
    # Order views
    path('order/lsit/', OrderListCreateView.as_view()),
    path('order/detil/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view())
]