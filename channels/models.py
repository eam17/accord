from django.db import models
from servers.models import Server

class Channel(models.Model):
    channel_id = models.AutoField(primary_key=True)
    display_name = models.CharField(max_length=100)
    TEXT = 'text'
    VOICE = 'voice'
    type_choices = [
        (TEXT, 'Text'),
        (VOICE, 'Voice'),
    ]
    type = models.CharField(
        max_length=5,
        choices=type_choices,
        default='text',
        blank=False,
    )
    server = models.ForeignKey('servers.Server', on_delete=models.CASCADE,)
    def __str__(self):
        return self.display_name+" "+self.type