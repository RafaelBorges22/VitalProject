from django.db import models
from uuid import uuid4

class MotoristModel(models.Model):
    id_motorist = models.AutoField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    cnh = models.CharField(max_length=255)
    veiculo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.cnh} - {self.veiculo}"