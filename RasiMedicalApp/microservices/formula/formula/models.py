from django.db import models


class Formula(models.Model):
    dose = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    unity = models.CharField(max_length=255)
    medicationId = models.IntegerField()
    presentation = models.CharField(max_length=255)

    def __str__(self):
        return f"Formula -> MedicationId {self.medicationId}. Dose {self.dose}{self.unity}. Frecuency {self.frequency}"
