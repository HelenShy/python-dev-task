from django.db import models
import requests

from crm.applications.consts import ERP_HOSTNAME


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
        login_url = 'http://127.0.0.1:8001/api/v2/login/'   # TODO: hostname нужно вынести в константы
        auth = requests.post(login_url, data = {'username': 'admin',
                                                'password': 'skorost123'})  # TODO: лонин и пароль вынести в константы
        if auth.status_code == 401:
            return "ERROR: User cannot be authorised."
        elif auth.status_code != 200:
            return "ERROR: Connection to payments` api cannot be established."
        token = auth.json()['token']
        payments_url = '{}/api/v2/agreements/{}/payments/'.format(ERP_HOSTNAME, self.agreement_id)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + token
        }

        resp = requests.get(payments_url, headers=headers)
        return resp.json()

# TODO: множественное нарушение PEP8
