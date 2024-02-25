from django.urls import path
from .views import CounsellorAPIView

urlpatterns = [
    path('list/', CounsellorAPIView.as_view(), name='counsellor_list'),
    path('create/', CounsellorAPIView.as_view(), name='counsellor_create'),
    path('update/<int:pk>/', CounsellorAPIView.as_view(), name='counsellor_update'),
    path('delete/<int:pk>/', CounsellorAPIView.as_view(), name='counsellor_delete'),
]