from django.db import models


    
class Module(models.Model):
    title = models.CharField(max_length=255)
    cards = models.JSONField(blank=True)

    def __str__(self):
        return self.title


