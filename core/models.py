from django.db import models

# Create your models here.
class StartUpInternships(models.Model):
    startup_name = models.CharField(max_length=40)
    startup_contact_name = models.CharField(max_length=30)
    startup_contact_email = models.EmailField()
    startup_contact_phone = models.CharField(max_length=20)
    incentive = models.IntegerField()
    description_file = models.FileField(upload_to ='media/attachments/%Y/%m/')
    startup_website = models.URLField()