from urllib import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

from qpd_api import serializers
from qpd_logic import runjob


class JobApiView(APIView):
    """Logic for Job Endpoint"""

    serializer_class = serializers.JobSerializer

    def post(self, request):
        """Creates Job object"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(request.data)
            # job = json.loads(request.data)

            # runjob(job)
            return Response(
                "Job sent.",
                status=status.HTTP_200_OK,
            )

        return Response(
            "Invalid data.",
            status=status.HTTP_400_BAD_REQUEST,
        )
