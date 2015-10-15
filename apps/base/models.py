from django.db.models import *


class BaseMasterModel(Model):
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
