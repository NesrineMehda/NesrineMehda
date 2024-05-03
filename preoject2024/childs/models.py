from django.db import models
from django.contrib.auth.models import User
from datetime import date
      

      
         
      

class Child(models.Model):
      gendre_choises=[
       ('boy','boy') ,
       ('girl','girl'),
       ]
      firstname=models.CharField(max_length=50)
      lastname=models.CharField(max_length=50)
      gendre= models.CharField(max_length=10,choices=gendre_choises)
      DateofBirth=models.DateField()
      height=models.FloatField()
      wieght=models.FloatField()
      #mother=models.ForeignKey(Mother,on_delete=models.CASCADE ,default=None)
      #objects = ChildManager()
      
      def __str__(self):
          return self.firstname
      def age_in_days(self):
        today = date.today()
        delta_in_days = today - self.DateofBirth
        return delta_in_days.days
      

     
      @property
      def age(self):
        today = date.today()
        dob = self.DateofBirth

        # Calculate age in years
        age_years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        # Calculate age in months
        age_months = today.month - dob.month
        if age_months < 0:
            age_years -= 1
            age_months += 12

        # Calculate age in days
        
            # Find the l
      
        age_days = today.day - dob.day
        if age_days< 0:
            #st day of the previous month
            today_month = today.month - 1 if today.month > 1 else 12
            last_day_prev_month = 31 if today_month in [1, 3, 5, 7, 8, 10, 12] else 30 if today_month != 2 else 28
            age_days += last_day_prev_month

        return age_years, age_months, age_days
