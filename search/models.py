from django.db import models


class Emoji(models.Model):
    name = models.CharField(
        max_length=50,
    )
    code = models.CharField(
        max_length=50,
    )
