from django.db import models
from user_models.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(designation=User.Designations.STUDENT)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_year = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(5)]
    )

class Student(User):

    objects = StudentManager()

    class Meta:
        proxy = True

    @property
    def more(self):
        return self.studentprofile

    def save(self, *args, **kwargs):
        if not self.pk:
            self.designation = User.Designations.STUDENT
        
        return super().save(*args, **kwargs)

