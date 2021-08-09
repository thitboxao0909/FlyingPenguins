from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='pdfs/%Y/%m/%d')
# Create your models here.
