from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import TableUser

class DataSerializer(serializers.Serializer):
    json_data = serializers.JSONField()

    def create(self,validated_data):
        return TableUser.objects.create(username=User.username.field,json_data=validated_data)



