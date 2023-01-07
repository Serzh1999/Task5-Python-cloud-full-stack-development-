from django.db import models

# Create your models here.
class Message (models.Model):
    userA = models.CharField(max_length=100, blank=True, null=True)
    userB = models.CharField(max_length=100, blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    date = models.DateTimeField (auto_now_add=True, blank=True, null=True)


    def __str__(self):
        if len(self.msg) > 50:
            return self.msg[:50]+"..."
        return self.msg
