from django.db import models
import requests

from crm.applications.consts import ERP_HOSTNAME
from crm.applications.erp_api import ErpAdapter


class Application(models.Model):
    name = models.CharField(max_length=64)
    agreement_id = models.CharField(max_length=64, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # TODO: нет класса Meta, не критично

    class Meta:
        db_table = 'application'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @property
    def payments(self):     # TODO: метод нигде не используется
        """
        Returns payments list for agreement_id defined in application.
        """
        adapter = ErpAdapter(self.agreement_id)
        payments = adapter.adapt()
        return payments

# TODO: множественное нарушение PEP8
