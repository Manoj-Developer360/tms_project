from django.db import models

class LoginUser(models.Model):

    Mobile_number = models.CharField(max_length=10, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Mobile_number