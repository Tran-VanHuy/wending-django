from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Story(models.Model):
    image = models.FileField(upload_to="static/images", unique=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField()
    date = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

