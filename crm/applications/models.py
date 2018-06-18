from django.db import models
import requests
from django.conf import settings
# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=64)
    agreement_id = models.CharField(max_length=64, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # TODO: нет класса Meta, не критично

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
        if auth.status_code != 200:
            return "ERROR: Connection to payments` api cannot be established."
        token = auth.json()['token']
        payments_url = ('http://127.0.0.1:8001/api/v2/agreements/'
                        + self.agreement_id + '/payments/')
        headers = {'Content-Type': 'application/json',
                    'Authorization': 'Token ' + token}
        resp = requests.get(payments_url, headers=headers)  # TODO: нет проверки на статус ответа
        if resp.json() == []:   # TODO: не pythonic style. Надо писать вот так if resp.json():
            return "There are no payments for this agreement yet."
        data = ""
        for i in resp.json():
            # TODO: Лучше делать в блоке try catch, потому что могут быть ошибки типа KeyError
            data += "Payment ID: " + str(i['id']) + "\n"
            data += "Amount: " + str(i['amount']) + "\n"
            data += "Date: " + str(i['date']) + "\n"
            data += "\n"
        return data

# TODO: множественное нарушение PEP8
