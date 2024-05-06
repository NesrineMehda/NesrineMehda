from django.db import models
from django.utils.translation import gettext_lazy as _
from childs.models import *
from django.contrib.auth.models import User

class Fever(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE,default=None)
    child = models.ForeignKey(Child ,on_delete=models.CASCADE,default=None)
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
    #objects = FeverManager()
    
    def fever_instance(self):
          child=self.child
          temperature =self.temperature 
          irritability=self.irritability
          difficulty_breathing=self.difficulty_breathing
          chronic_diseases=self.chronic_diseases
          tummy_ache=self.tummy_ache
          lack_of_activity=self.lack_of_activity
          fever=self.fever
          cough=self.cough
          runny_nose=self.runny_nose
          vomiting=self.vomiting
          dehydration=self.dehydration
          diarrhea=self.diarrhea

          if temperature >= 38.0:
            if child.age_in_days() < 90:
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






    def __str__(self):
        return f"Fever - Temperature: {self.temperature}, Result: {self.result}"
