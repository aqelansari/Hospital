from rest_framework import serializers
from .models import Appointment
from patient.models import Patient
from counsellor.models import Counsellor


class AppointmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Appointment
        fields = '__all__'


    def validate(self, data):
        patient = data.get('patient')
        counsellor = data.get('counsellor')

        if not patient.is_active:
            raise serializers.ValidationError("The patient is not active.")
        if not counsellor.is_active:
            raise serializers.ValidationError("The counsellor is not active.")
        
        # Assuming is_active is a field indicating whether the appointment is active.
        existing_patient_appointment = Appointment.objects.filter(patient=patient, is_active=True).exclude(pk=self.instance.pk if self.instance else None)
        if existing_patient_appointment.exists():
            raise serializers.ValidationError("This patient already has an active appointment.")

        existing_counsellor_appointment = Appointment.objects.filter(counsellor=counsellor, is_active=True).exclude(pk=self.instance.pk if self.instance else None)
        if existing_counsellor_appointment.exists():
            raise serializers.ValidationError("This counsellor already has an active appointment.")

        return data

    def create(self, validated_data):
        validated_data['is_active'] = True
        appointment = Appointment.objects.create(**validated_data)
        return appointment
    
    def update(self, instance, validated_data):
        instance.patient = validated_data.get('patient', instance.patient)
        instance.counsellor = validated_data.get('counsellor', instance.counsellor)
        instance.appointment_date = validated_data.get('appointment_date', instance.appointment_date)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance