from rest_framework import serializers
from qpd_api import models


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = "__all__"
