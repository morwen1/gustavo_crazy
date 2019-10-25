from django.db import models


class CrazyAbstract(models.Model):
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField()

    class Meta:
        abstract = True