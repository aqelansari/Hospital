from django.urls import path
from .views import PatientAPIView

urlpatterns = [
    path('list/', PatientAPIView.as_view(), name='patient_list'),
    path('create/', PatientAPIView.as_view(), name='patient_create'),
    path('update/<int:pk>/', PatientAPIView.as_view(), name='patient_update'),
    path('delete/<int:pk>/', PatientAPIView.as_view(), name='patient_delete'),
]