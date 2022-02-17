from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField()
    uptime = models.DateTimeField(auto_now=True)
    creation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title[0:30]

    class Meta:
        ordering = ['-uptime']