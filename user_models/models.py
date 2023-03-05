from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    class Designations(models.TextChoices):
        STUDENT = ('STUDENT', 'Student')
        FACULTY = ('FACULTY', 'Faculty')

    class Departments(models.TextChoices):
        NO_DEPARTMENT = ('NO_DEPARTMENT', '-------------')
        B_TECH = ('B_TECH', 'B.Tech')
        M_TECH = ('M_TECH', 'M.Tech')
        BCA = ('BCA', 'BCA')
        BSC_IT = ('BSC_IT', 'Bsc.IT')
        MCA = ('MCA', 'MCA')
        MSC_IT = ('MSC_IT', 'MSc.IT')
        ARTS = ('ARTS', 'Arts')
        BBA = ('BBA', 'BBA')
        MBA = ('MBA', 'MBA')
        LAW = ('LAW', 'Law')
        MBBS = ('MBBS', 'MBBS')
        ARCHITECTURE = ('ARCHITECTURE', 'Architecture')
        DIPLOMA = ('DIPLOMA', 'Diploma')
        

    designation = models.CharField(max_length=30, choices=Designations.choices)
    department = models.CharField(max_length=30, choices=Departments.choices, default=Departments.NO_DEPARTMENT)
    is_elevated = models.BooleanField(default=False)

class Followings(models.Model):
    user_id = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_id}::{self.following_user_id}'