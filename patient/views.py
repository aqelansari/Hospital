from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework  import status
from .serializers import PatientSerializer
from .models import Patient, User



class PatientAPIView(APIView):
    def get(self, request, format=None):
        patient_data = Patient.objects.filter(is_active=True)
        serializer = PatientSerializer(patient_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Patient_email = serializer.validated_data.get('email')
            User.objects.filter(email=Patient_email).update(is_patient=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            patient_profile = Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            return Response({'error': 'Patient not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PatientSerializer(patient_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        try:
            patient_profile = Patient.objects.get(pk=pk)
            patient_profile.is_active = False
            patient_profile.save()
            return Response({'error':'patient delete successfully', 'error_code':'204', 'data':{}},
                                status=status.HTTP_204_NO_CONTENT)
        except Patient.DoesNotExist:
            return Response({'error': 'Patient not found.', 'error_code':'404', 'data':{}},
                             status=status.HTTP_404_NOT_FOUND)


