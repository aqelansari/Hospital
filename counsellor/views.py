from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework  import status
from .serializers import CounsellorSerializer
from .models import Counsellor
from patient.models import User



class CounsellorAPIView(APIView):
    def get(self, request, format=None):
        counsellor_data = Counsellor.objects.filter(is_active=True)
        serializer = CounsellorSerializer(counsellor_data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CounsellorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            counsellor_email = serializer.validated_data.get('email')
            User.objects.filter(email=counsellor_email).update(is_counsellor=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            counsellor_profile = Counsellor.objects.get(pk=pk)
        except Counsellor.DoesNotExist:
            return Response({'error': 'Counsellor not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CounsellorSerializer(counsellor_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        try:
            counsellor_profile = Counsellor.objects.get(pk=pk)
            counsellor_profile.is_active = False
            counsellor_profile.save()
            return Response({'error':'Counsellor delete successfully', 'error_code':'204', 'data':{}},
                                status=status.HTTP_204_NO_CONTENT)
        except Counsellor.DoesNotExist:
            return Response({'error': 'Counsellor not found.', 'error_code':'404', 'data':{}},
                             status=status.HTTP_404_NOT_FOUND)


