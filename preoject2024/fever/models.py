from django.db import models
from django.utils.translation import gettext_lazy as _
from childs.models import *


class FeverManager(models.Manager):
    def categorize_fever(self, temperature, age_in_days, fever, cough, runny_nose,
                         difficulty_breathing, diarrhea, vomiting, dehydration,
                         lack_of_activity, irritability, chronic_diseases, tummy_ache ):
                          
        temperature = float(temperature)

        if temperature >= 38.0:
            if age_in_days < 90:
                result = "Child under 90 days - Consult a doctor immediately."
            elif irritability or difficulty_breathing or chronic_diseases or tummy_ache or lack_of_activity:
                    result = "Child has symptoms - Consult a doctor immediately."
            elif fever or cough or runny_nose or vomiting or dehydration or diarrhea:
                    result = "Child has symptoms - Consult a doctor."
            else:
                    result = "Child is fine. Monitor for changes."
        else:
            result = "Child is fine. Monitor for changes."
        
        return result

class Fever(models.Model):
    temperature = models.DecimalField(_("Temperature"), max_digits=5, decimal_places=2)
    fever = models.BooleanField(_("Fever"), default=False)
    cough = models.BooleanField(_("Cough"), default=False)
    runny_nose = models.BooleanField(_("Runny Nose"), default=False)
    difficulty_breathing = models.BooleanField(_("Difficulty Breathing"), default=False)
    diarrhea = models.BooleanField(_("Diarrhea"), default=False)
    vomiting = models.BooleanField(_("Vomiting"), default=False)
    dehydration = models.BooleanField(_("Dehydration"), default=False)
    lack_of_activity = models.BooleanField(_("Lack of Activity"), default=False)
    irritability = models.BooleanField(_("Irritability"), default=False)
    chronic_diseases= models.BooleanField(_("Chronic diseases"), default=False)
    tummy_ache= models.BooleanField(_("Tummy_ache"), default=False)
    others = models.TextField(_("Other Symptoms"), blank=True)
    result = models.CharField(_("Result"), max_length=255,default="yes")
    #fever_duration = models.PositiveSmallIntegerField("Fever Duration (days)", default=0)
    #diarrhea_duration = models.PositiveSmallIntegerField("Diarrhea Duration (days)", default=0)
    objects = FeverManager()

    def __str__(self):
        return f"Fever - Temperature: {self.temperature}, Result: {self.result}"

    


  



