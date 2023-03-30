from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateTimeField()

    def __str__(self):
        return self.nome


class Curso(models.Model):
    NIVEL = (
        ('B', 'Basico'),
        ('I', 'Intermediario'),
        ('A', 'Avançado'),
    )

    codigo_curso = models.CharField(max_length=10, blank=False, null=False,)
    descricao = models.CharField(max_length=100, blank=False, null=False,)
    nivel = models.CharField(max_length=1, blank=False, null=False, choices=NIVEL, default='B')

    def __str__(self):
        return self.descricao


class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, blank=False, null=False, choices=PERIODO, default='M')
