from django.db import models

from core.models import ClientUser
from user_management.models import Organization


class Tag(models.Model):
    """
    A trait, label, or group for a set of users.

    Tags can be used to categorize and group ClientUser objects into sub groups.
    """
    name = models.SlugField()
    user = models.ManyToManyField(ClientUser)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
