from rest_framework.serializers import ModelSerializer
from .models import Monkey

class MonkeySerializer(ModelSerializer):
  class Meta:
    fields = ('id', 'owner', 'name', 'tude', 'birth_info')
    model = Monkey
