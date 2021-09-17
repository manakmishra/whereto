from django.db import models
import uuid

# Create your models here.
class URL(models.Model):
    link = models.CharField(max_length = 1000)
    new = models.CharField(max_length = 6)
    uid = models.UUIDField(primary_key = True, default=uuid.uuid4(), editable = True, max_length=36)