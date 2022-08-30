from .models import Monkey
from .serializers import MonkeySerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics

class MonkeyList(generics.ListCreateAPIView):
  queryset = Monkey.objects.all()
  serializer_class = MonkeySerializer

class MonkeyDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Monkey.objects.all()
  serializer_class = MonkeySerializer
