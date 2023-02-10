import uuid
from django.db import models
from user_models.models import User
from ckeditor.fields import RichTextField 

# Create your models here.
class News(models.Model):
    news_id = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='approved_by_name')
    department = models.CharField(max_length=30, choices=User.Departments.choices, default=User.Departments.NO_DEPARTMENT)
    introduction = models.CharField(max_length=100, null=True)
    link_to_banner = models.URLField(max_length=255, null=True, blank=True, default=None)

    def __str__(self):
        return self.headline
