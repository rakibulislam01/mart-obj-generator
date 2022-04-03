from .views import GenerateObjAPIView, ReportAPIView, HomeView
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('api/generate-obj/', GenerateObjAPIView.as_view(), name='generate_obj'),
    path('api/report/', ReportAPIView.as_view(), name='report'),
]
