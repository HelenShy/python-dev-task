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

