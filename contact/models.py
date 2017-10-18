from django.db import models

class ContactMe(models.Model):
    name = models.CharField(max_length = 240)
    email = models.CharField(max_length = 240)
    message = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name
