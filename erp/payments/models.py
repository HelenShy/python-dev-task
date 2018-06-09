from django.db import models
from django.conf import settings

import json


class AgreementManager(models.Manager):
    def all(self):
        with open(settings.BASE_DIR + '\payments.json') as file:
            data = str(file.read())
        p = json.loads(data,  object_hook = as_agreement)
        return p

    def by_id(self, agreement_id):
        resp = [agr for agr in Agreement.objects.all() if agr.id==agreement_id]
        if len(resp) > 0:
            return resp[0]
        return None


def as_agreement(dct):
    return Agreement(dct['agreement_id'])


class Agreement(models.Model):
    objects = AgreementManager()

    def __init__(self, id,  *args, **kwargs):
        super(Agreement, self).__init__(*args, **kwargs)
        self.id = id

    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class PaymentManager(models.Manager):
    def all(self):
        with open(settings.BASE_DIR + '\payments.json') as file:
            data = str(file.read())
        p = json.loads(data,  object_hook = as_payment)
        return p

    def by_agreement_id(self, agreement_id):
        resp = [paym for paym in Payment.objects.all() if paym.agreement.id==agreement_id]
        return resp

    def by_id(self, agreement_id, id):
        resp = [paym for paym in Payment.objects.all() if paym.agreement.id==agreement_id and paym.id==id]
        if len(resp) > 0:
            return resp[0]
        return None


def as_payment(dct):
    agreement = Agreement(dct['agreement_id'])
    return Payment(dct['id'], agreement, dct['amount'], dct['date'])


class Payment(models.Model):
    agreement = models.ForeignKey('Agreement', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date = models.DateTimeField()

    objects = PaymentManager()

    def __init__(self, id, agreement, amount, date, *args, **kwargs):
        super(Payment, self).__init__(*args, **kwargs)
        self.id = id
        self.agreement = agreement
        self.amount = amount
        self.date = date

    def __str__(self):
        return str(self.agreement)

    def __repr__(self):
        return str(self.agreement)
