from django.db import models

from apps.tests.choices import CorrectAnswerChoices
from apps.topics.models import Topics


class Tests(models.Model):
    description = models.TextField()
    question = models.TextField()
    a = models.TextField()
    b = models.TextField()
    c = models.TextField()
    d = models.TextField()
    correct_answer = models.CharField(choices=CorrectAnswerChoices.choices)
    topic = models.ForeignKey(Topics, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Tests"

    def __str__(self):
        return f"{self.topic}"
