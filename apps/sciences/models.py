from django.db import models


class Sciences(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Science"
        verbose_name_plural = "Sciences"

    def __str__(self):
        return f"{self.name}"
