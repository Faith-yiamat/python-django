from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length= 20)
    date_of_birth = models.DateField()
    email = models.EmailField()
    course = models.CharField(max_length= 20)
    gender = models.CharField(max_length= 20)
    id_number = models.PositiveSmallIntegerField()
    years_of_experience = models.PositiveSmallIntegerField()
    nationality = models.CharField(max_length= 20)
    coutry = models.CharField(max_length= 20)
 

    def __str__ (self):
        return f"{self.first_name} {self.last_name}"
