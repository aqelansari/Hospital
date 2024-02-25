from django.urls import path
from .views import AppointmentAPIView,AppointmentsByPatientAPIView,\
    AppointmentsByCounsellorAPIView, AppointmentsByDateRangeAPIView

urlpatterns = [
    path('list/', AppointmentAPIView.as_view(), name='appointment_list'),
    path('create/', AppointmentAPIView.as_view(), name='appointment_create'),
    path('update/<int:pk>/', AppointmentAPIView.as_view(), name='appointment_update'),
    path('delete/<int:pk>/', AppointmentAPIView.as_view(), name='appointment_delete'),
    path('patient/<int:patient_id>/', AppointmentsByPatientAPIView.as_view(), name='appointments_by_patient'),
    path('counsellor/<int:counsellor_id>/', AppointmentsByCounsellorAPIView.as_view(), name='appointments_by_counsellor'),
    path('filter/daterange/', AppointmentsByDateRangeAPIView.as_view(), name='appointments_filter_by_daterange'),
]