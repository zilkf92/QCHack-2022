from rest_framework.views import APIView
from rest_framework.response import Response


class JobApiView(APIView):
    """Logic for Job Endpoint"""

    def post(self, request, format=None):
        """Creates Job object"""
