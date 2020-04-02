from django.db import models
from django.contrib.auth.models import User

class Server(models.Model):
    server_id = models.AutoField(primary_key=True)
    display_name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="server")
    def __str__(self):
        return self.display_name