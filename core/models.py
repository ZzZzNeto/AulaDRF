from django.db import models

# Create your models here.

class Turma(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=100)
    max_alunos = models.IntegerField()

class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    matricula = models.CharField(max_length=10, unique=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    