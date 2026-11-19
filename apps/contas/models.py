from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
    class Perfil(models.TextChoices):
        GERENTE = "GERENTE", "Gerente"
        VENDEDOR = "VENDEDOR", "Vendedor"
        ESTOQUISTA = "ESTOQUISTA", "Estoquista"

    perfil = models.CharField(
        "perfil",
        max_length=12,
        choices=Perfil.choices,
        default=Perfil.VENDEDOR,
    )

    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"

    def __str__(self):
        return self.username