import uuid
from django.db import models
from user_models.models import User

# Create your models here.
class News(models.Model):
    news_id = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    content = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='approved_by_name')
    department = models.CharField(max_length=30, choices=User.Departments.choices, default=User.Departments.NO_DEPARTMENT)

    def __str__(self):
        return self.headline
