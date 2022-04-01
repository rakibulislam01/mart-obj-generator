from .views import TestAPIView
from django.urls import path

urlpatterns = [
    path('', TestAPIView.as_view(), name='test_view'),
]
