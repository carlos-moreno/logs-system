import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from codenation.account.models import User


class Agent(models.Model):
    ENVIRONMENTS = [(env, env) for env in ["PRODUCTION", "HOMOLOGATION", "DEVELOPMENT"]]

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("name"), max_length=50, help_text="Agent name.")
    status = models.BooleanField(_("status"), default=True, help_text="Agent status.")
    environment = models.CharField(
        _("environment"),
        max_length=15,
        choices=ENVIRONMENTS,
        help_text="Agent environment type.",
    )
    version = models.CharField(_("version"), max_length=5, help_text="Agent version.")
    address = models.GenericIPAddressField(
        _("ip address"), help_text="Agent ip address.", unique=True
    )

    class Meta:
        db_table = "agent"
        ordering = ("-status",)

    def __str__(self):
        return f"{self.environment} : {self.name} : {self.address}"


class Event(models.Model):
    LEVELS = [
        (level, level) for level in ["CRITICAL", "DEBUG", "ERROR", "WARNING", "INFO"]
    ]

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    level = models.CharField(
        _("level"), max_length=20, choices=LEVELS, help_text="Event level."
    )
    message = models.TextField(
        _("message"), help_text="Message pertinent to the event."
    )
    shelved = models.BooleanField(
        _("shelved"), default=False, help_text="Event has been shelved."
    )
    received_in = models.DateField(
        _("received in"), auto_now_add=True, help_text="Date of received of the event."
    )
    occurrences = models.IntegerField(
        _("occurrences"),
        blank=True,
        editable=False,
        help_text="Number of event occurrences.",
    )
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "event"
        ordering = ("-received_in",)

    def __str__(self):
        return f"{self.level} : {self.agent.environment} : {self.agent.address}"

    def save(self, *args, **kwargs):
        if not self.occurrences:
            self.occurrences = self.number_of_occurrences()
        super(Event, self).save(*args, **kwargs)

    def number_of_occurrences(self):
        return (
            Event.objects.filter(
                level=self.level, agent=self.agent, message=self.message
            ).count()
            + 1
        )
