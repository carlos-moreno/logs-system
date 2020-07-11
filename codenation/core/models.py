import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from codenation.account.models import User


class Agent(models.Model):
    ENVIRONMENTS = [
        (env, env) for env in ["PRODUCTION", "HOMOLOGATION", "DEVELOPMENT"]
    ]

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("name"), max_length=50)
    status = models.BooleanField(_("status"), default=True)
    environment = models.CharField(
        _("environment"), max_length=15, choices=ENVIRONMENTS
    )
    version = models.CharField(_("version"), max_length=5)
    address = models.GenericIPAddressField(_("ip address"))

    class Meta:
        db_table = "agent"

    def __str__(self):
        return f"{self.environment} : {self.name} : {self.address}"


class Event(models.Model):
    LEVELS = [
        (level, level) for level in ["CRITICAL", "DEBUG", "ERROR", "WARNING", "INFO"]
    ]

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    level = models.CharField(_("level"), max_length=20, choices=LEVELS)
    message = models.TextField(_("message"))
    shelved = models.BooleanField(_("shelved"), default=False)
    received_in = models.DateField(_("received in"), auto_now_add=True)
    occurrences = models.IntegerField(_("occurrences"), editable=False)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "event"

    def __str__(self):
        return f"{self.level} : {self.agent.environment} : {self.agent.address}"

    def save(self, *args, **kwargs):
        self.occurrences = self.number_of_occurrences()
        super(Event, self).save(*args, **kwargs)

    def number_of_occurrences(self):
        return (
            Event.objects.filter(
                level=self.level, agent=self.agent, message=self.message
            ).count()
            + 1
        )
