from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Palco(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.IntegerField()
    acessibilidade_mobilidade_reduzida = models.BooleanField(default=False)  # NOVO CAMPO

    def __str__(self):
        return self.nome


class Dia(models.Model):
    data = models.DateField()

    class Meta:
        ordering = ["data"]  # GARANTE DIAS ORDENADOS CRESCENTEMENTE

    def __str__(self):
        return str(self.data)


class Concerto(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    palco = models.ForeignKey(Palco, on_delete=models.CASCADE)
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE)
    hora = models.TimeField()

    class Meta:
        ordering = ["dia__data", "hora"]  # ORDENA POR DIA E HORA

    def __str__(self):
        return f"{self.banda} - {self.dia} {self.hora}"
