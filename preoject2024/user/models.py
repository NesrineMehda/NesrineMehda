from django.db import models

# Create your models here.
class User(models.Model):
      
      firstname=models.CharField(max_length=50)
      lastname=models.CharField(max_length=50)
      username = models.CharField(max_length=10 ,unique =True)
      email =models.EmailField( unique =True)
      password= models.CharField(max_length=50)
      def __str__(self):
            return self.firstname
