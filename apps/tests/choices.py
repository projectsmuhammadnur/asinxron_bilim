from django.db import models


class CorrectAnswerChoices(models.TextChoices):
    A = ("a", "A")
    B = ("b", "B")
    C = ("c", "C")
    D = ("d", "D")
