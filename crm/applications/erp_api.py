import requests
from django.conf import settings
from crm.applications.consts import ERP_HOSTNAME


class ErpAdapter:

    def __init__(self, agreement_id):
        self.agreement_id = agreement_id

    def _login(self):
        login_url = '{}/api/v2/login/'.format(ERP_HOSTNAME)
        data = {
            'username': settings.PAYMENTS_API_NAME,
            'password': settings.PAYMENTS_API_PASSWORD
        }
        auth_resp = requests.post(url=login_url, data=data)
        if auth_resp.status_code == 401:
            return True, "ERROR: User cannot be authorised."
        elif auth_resp.status_code != 200:
            return True, "ERROR: Connection to payments` api cannot be established."
        token = auth_resp.json()['token']
        return False, token

    def _get_payments(self, agreement_id, token):
        payments_url = '{}/api/v2/agreements/{}/payments/'.format(ERP_HOSTNAME, agreement_id)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + token
        }

        resp = requests.get(payments_url, headers=headers)
        if 200 >= resp.status_code <= 299:
            return False, resp.json()
        else:
            return True, "Error"

    def adapt(self):
        is_error, data = self._login()
        if is_error:
            return data

        token = data

        is_payments_err, payments_data = self._get_payments(self.agreement_id, token)
        if is_payments_err:
            return {}
        else:
            return payments_data

    def fin_info_on_date(self, agreement_id, date):

