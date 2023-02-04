from django.db import models
from user_models.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(designation=User.Designations.STUDENT)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_year = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
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


@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created and instance.designation == User.Designations.STUDENT:
        StudentProfile.objects.create(
            user = instance,
        )
