from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='', blank=True)
    position = models.CharField(max_length=255, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Price_oofer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name