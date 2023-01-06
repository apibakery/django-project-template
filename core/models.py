from django.db import models


class Hello(models.Model):
    """
    Example model
    """

    message = models.CharField(
        max_length=255,
        blank=True,
        default="world",
        help_text="A welcome message stored in this model instance",
    )

    def __str__(self):
        return str(self.message)
