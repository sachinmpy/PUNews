from django.db import models
from user_models.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class FacultyManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(designation=User.Designations.FACULTY)

class FacultyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Faculty(User):

    objects = FacultyManager()
    
    class Meta:
        proxy = True

    @property
    def more(self):
        return self.facultyprofile
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.designation = User.Designations.FACULTY
        
        return super().save(*args, **kwargs)
    

@receiver(signal=post_save, sender=User)
def create_faculty_profile(sender, instance, created, **kwargs):
    if created and instance.designation == User.Designations.FACULTY:
        FacultyProfile.objects.create(
            user = instance,
        )
        