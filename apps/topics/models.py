from django.db import models

from apps.sciences.models import Sciences


class Topics(models.Model):
    name = models.CharField(max_length=255, unique=True)
    science = models.ForeignKey(Sciences, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self):
        return f"{self.name}"
