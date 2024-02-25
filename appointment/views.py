from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework  import status
from datetime import datetime
from django.db.models import Q
from .serializers import AppointmentSerializer
from .models import Appointment
from patient.models import User


class AppointmentAPIView(APIView):
    def get(self, request, format=None):
        appointment_data = Appointment.objects.filter(is_active=True)
        serializer = AppointmentSerializer(appointment_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = request.user 
        # if not user.is_active or (not user.is_patient and not user.is_counsellor):
        #     return Response({"error": "Inactive or unauthorized user cannot create appointments."},
        #                     status=status.HTTP_403_FORBIDDEN)
        # active_appointments = Appointment.objects.filter((Q(patient=user) | Q(counsellor=user)), is_active=True)
        # if active_appointments.exists():
        #     return Response({"error": "User already has an active appointment."},
        #                 status=status.HTTP_400_BAD_REQUEST)
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            appointment_profile = Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AppointmentSerializer(appointment_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        try:
            appointment_profile = Appointment.objects.get(pk=pk)
            appointment_profile.is_active = False
            appointment_profile.save()
            return Response({'error':'Appointment delete successfully', 'error_code':'204', 'data':{}},
                                status=status.HTTP_204_NO_CONTENT)
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found.', 'error_code':'404', 'data':{}},
                             status=status.HTTP_404_NOT_FOUND)


class AppointmentsByPatientAPIView(APIView):
    def get(self, request, patient_id):
        appointments = Appointment.objects.filter(patient__id=patient_id, is_active=True)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    
class AppointmentsByCounsellorAPIView(APIView):
    def get(self, request, counsellor_id):
        appointments = Appointment.objects.filter(counsellor__id=counsellor_id, is_active=True)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    

class AppointmentsByDateRangeAPIView(APIView):
    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not start_date or not end_date:
            return Response({"error": "Both start_date and end_date parameters are required."}, status=400)

        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

        appointments = Appointment.objects.filter(
            is_active=True,
            appointment_date__range=(start_date, end_date)
        ).order_by('-appointment_date')

        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)