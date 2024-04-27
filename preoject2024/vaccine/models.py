from django.db import models


class VaccinManager(models.Manager):
    def nearest_vaccine_for_child(self,child):
        # Get the child's age in days
        child_age_in_days = child.age_in_days()

        # Query for vaccines with recommended ages greater than the child's age
        nearest_vaccines = self.filter(ageindays__gte=child_age_in_days)

        # If there are no vaccines with recommended ages greater than the child's age,
        # then get the vaccine with the closest recommended age
        if not nearest_vaccines.exists():
            nearest_vaccine = self.order_by('ageindays').first()
        else:
            nearest_vaccine = nearest_vaccines.order_by('ageindays').first()

        return nearest_vaccine

class Vaccin(models.Model):
       name =models.CharField(max_length=50)
       completed=models.BooleanField(default=False)
       decsription=models.CharField(max_length=500,null=True)
       ageindays =models.IntegerField() 
       objects = VaccinManager()

       def __str__(self):
          return self.name
