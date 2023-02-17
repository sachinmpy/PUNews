import uuid
from django.db import models
from user_models.models import User

# Create your models here.
class Post(models.Model):
    post_id = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4, editable=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
    posted_date = models.DateTimeField(auto_now_add=True)
    is_global = models.BooleanField(default=False)