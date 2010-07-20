from django.db import models

class Topico(models.Model):
    """representa um topico"""
    titulo = models.CharField(max_length=64)
class Resposta(models.Model):
    '''Uma resposta no topico'''
    texto = models.CharField(max_length=140)
    topico = models.ForeignKey(Topico, related_name='replies')

