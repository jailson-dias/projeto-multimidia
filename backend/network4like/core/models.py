from django.db import models

# Create your models here.
class Imagem(models.Model):
	file = models.ImageField("Arquivo", default="")
	qtd_likes = models.PositiveIntegerField('Quantidade de Likes', null=True, blank=True)