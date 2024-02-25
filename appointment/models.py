from django.db import models
from patient.models import Patient
from counsellor.models import Counsellor


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    counsellor = models.ForeignKey(Counsellor, on_delete=models.DO_NOTHING)
    appointment_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'appointment'
