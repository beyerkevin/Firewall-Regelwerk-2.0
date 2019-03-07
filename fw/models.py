from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class FWData(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Host = models.CharField(max_length=50)
    date = models.DateTimeField(blank=True, null=True)
    description = models.TextField()

    def timestamp(self):
        self.date = timezone.now()
        self.save()


    def __Host__(self):
        return self.Host
        
    
    def __User__(self):
        return self.User

    def __description__(self):
        return self.description

