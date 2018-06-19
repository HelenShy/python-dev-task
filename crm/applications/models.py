from django.db import models
import requests
from django.conf import settings


class Application(models.Model):
    name = models.CharField(max_length=64)
    agreement_id = models.CharField(max_length=64, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @property
    def payments(self):
        """
        Returns payments list for agreement_id defined in application.
        """
        login_url = 'http://127.0.0.1:8000/api/v2/login/'
        auth = requests.post(login_url, data = {'username': 'admin',
                                                'password': 'skorost123'})
        if auth.status_code == 401:
            return "ERROR: User cannot be authorised."
        elif auth.status_code != 200:
            return "ERROR: Connection to payments` api cannot be established."
        token = auth.json()['token']
        payments_url = ('http://127.0.0.1:8000/api/v2/agreements/'
                        + self.agreement_id + '/payments/')
        headers = {'Content-Type': 'application/json',
                    'Authorization': 'Token ' + token}
        resp = requests.get(payments_url, headers=headers)
        return resp.json()
