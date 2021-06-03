from django.db import models

# Create your models here

class Equipamentos(models.Model):
    nome_equipamento = models.CharField(max_length=100)
    nome_display = models.CharField(max_length=100)
    idsectra = models.CharField(max_length=11)

    def __str__(self):
        return "{} ({})".format(self.nome_equipamento, self.nome_display)

class RevisaoManuais(models.Model):
    nome_equipamento = models.ForeignKey(Equipamentos, on_delete=models.PROTECT, related_name="manuais")
    ns_min = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='manuais/pdf')

    def __str__(self):
        return self.nome_equipamento.nome_equipamento