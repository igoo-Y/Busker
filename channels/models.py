from typing import Tuple
from django.db import models
from core import models as core_models
from users import models as user_models


class Channel(core_models.TimeStampedModel):

    """Channel Model Definition"""

    name = models.CharField(max_length=140)
    image = models.ImageField(upload_to="channel_photos", blank=True, null=True)
    on_air = models.BooleanField(default=False)
    channel_host = models.ForeignKey(
        "users.User",
        related_name="channel",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name