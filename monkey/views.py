from django.shortcuts import render
from .models import Monkey
from .serializers import MonkeySerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

class MonkeyList(ListCreateAPIView):
  queryset = Monkey.objects.all()
  serializer_class = MonkeySerializer

class MonkeyDetail(RetrieveDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Monkey.objects.all()
  serializer_class = MonkeySerializer
