# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Produto(models.Model):

    #__Produto_FIELDS__
    prd-cod = models.IntegerField(null=True, blank=True)
    prd-des = models.CharField(max_length=255, null=True, blank=True)
    prd-create = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Produto_FIELDS__END

    class Meta:
        verbose_name        = _("Produto")
        verbose_name_plural = _("Produto")


class Cliente(models.Model):

    #__Cliente_FIELDS__
    cli-ativo = models.BooleanField()

    #__Cliente_FIELDS__END

    class Meta:
        verbose_name        = _("Cliente")
        verbose_name_plural = _("Cliente")


class Pedido(models.Model):

    #__Pedido_FIELDS__
    cli-cod = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    #__Pedido_FIELDS__END

    class Meta:
        verbose_name        = _("Pedido")
        verbose_name_plural = _("Pedido")


class Pedidoprod(models.Model):

    #__Pedidoprod_FIELDS__
    ped-cod = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    prd-cod = models.ForeignKey(Produto, on_delete=models.CASCADE)
    ppr-qtd = models.IntegerField(null=True, blank=True)
    ppr-val = models.IntegerField(null=True, blank=True)

    #__Pedidoprod_FIELDS__END

    class Meta:
        verbose_name        = _("Pedidoprod")
        verbose_name_plural = _("Pedidoprod")



#__MODELS__END
