from rest_framework import serializers
from appt_api.models import User
class userSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  name = serializers.CharField()
  def create(self,data):
    return User.objects.create(**data)