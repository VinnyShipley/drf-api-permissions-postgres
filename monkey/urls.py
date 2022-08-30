from django.urls import path
from .views import MonkeyList, MonkeyDetail

urlpatterns = [
  path('', MonkeyList.as_view(), name='monkey_list'),
  path('<int>:pk/', MonkeyDetail.as_view(), name='monkey_detail')
]