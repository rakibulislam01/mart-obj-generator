from rest_framework import viewsets, views
from rest_framework.response import Response


class TestAPIView(views.APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request):
        return Response({
            "Test": 123
        })
