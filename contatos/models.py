from django.db import models
from django.utils import timezone   



# --------- A cada alteração realizada nas chaves, será necessário executar
# O comando python manage.py makemigrations e logo depois o python manage.py migrate
class Categoria (models.Model):
    nome = models.CharField (max_length = 255)

    def __str__(self):
        return self.nome
class Contato (models.Model):
    nome = models.CharField (max_length = 255)
    sobrenome = models.CharField (max_length = 255, blank = True)
    telefone = models.CharField (max_length = 255)
    email = models.CharField (max_length = 255, blank = True)

    data_criacao = models.DateTimeField (default = timezone.now)
    descricao = models.TextField (blank = True)
    
    categoria = models.ForeignKey(Categoria, on_delete = models.DO_NOTHING)

    mostrar = models.BooleanField (default=True)
    # Função usada para chamar o id nome para a pagina incial

    foto = models.ImageField (blank=True, upload_to = 'foto/%Y/%m/%m')




    def __str__(self):
        return self.nome


"""
CONTATOS
id: INT (automático)

nome: STR * (obrigatorio)
sobrenome: STR * (opcional)
telefone: STR * (obrigatorio)
e-mail: STR (opcional)

data_criacao: DATETIME (automático)
descrição: texto
categoria: CATEGORIA (outro model)

CATEGORIA
id: INT
nome: STR * (obrigatorio)

"""

