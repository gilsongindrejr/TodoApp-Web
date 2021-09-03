from django.db import models
from django.utils.translation import gettext_lazy as _


class Base(models.Model):
    created = models.DateField(_('Created'), auto_now_add=True)
    modified = models.DateField(_('Modified'), auto_now=True)
    active = models.BooleanField(_('Active'), default=True)

    class Meta:
        abstract = True


class Task(Base):
    task = models.CharField(_('Task'), max_length=200)
    date = models.DateTimeField(_('Date'))

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        return self.task
