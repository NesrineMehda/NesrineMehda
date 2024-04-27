from django.db import models
from django.utils.translation import gettext_lazy as _
from child.models import *

class FeverManager(models.Manager):
  def categorize_fever( self , temperature,age_in_days, fever, cough, runny_nose,
       difficulty_breathing, diarrhea, vomiting, dehydration, lack_of_activity, irritability,
         others):
    temperature = float(temperature)  
    if temperature >= 38.0: 

      if age_in_days < 90:
        result = "Child under 90 days - Consult a doctor immediately."
      elif fever  or cough or difficulty_breathing or dehydration:
        result = "Child has symptoms - Consult a doctor."
      elif vomiting or diarrhea or irritability:
        result = "Child needs medical attention."
      else:
        result = "Child is fine. Monitor for changes."
    else :
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
    others = models.TextField(_("Other Symptoms"), blank=True)
    result = models.CharField(_("Result"), max_length=255,default="yes")
    objects = FeverManager()

    def __str__(self):
        return f"Fever - Temperature: {self.temperature}"# Result: {self.result}"
