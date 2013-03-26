# -*- coding: utf-8 -*-

from django.db import models

class Anagrafica(models.Model):
    ragione_sociale = models.CharField(max_length=255)
    indirizzo = models.CharField(max_length=255, null=True, blank=True)
    comune = models.CharField(max_length=255, null=True, blank=True)
    provincia = models.CharField(max_length=3, null=True, blank=True)
    partita_iva = models.CharField(max_length=255, null=True, blank=True)
    codice_fiscale = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    referente = models.CharField(max_length=255, null=True, blank=True)
    tel_referente = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        abstract = True
        verbose_name_plural = 'Anagrafiche'



# class Cliente(Anagrafica):
#     pass


class Gruppo_orientativo_iva(models.Model):
    nome_gruppo = models.CharField(max_length=255)
    aliquota_orientativa = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Gruppi orientativi IVA'

    
    
class Iva(models.Model):
    gruppo_orientativo = models.ForeignKey(Gruppo_orientativo_iva)
    percentuale_aliquota = models.SmallIntegerField()
    etichetta = models.CharField(max_length=255)
    attiva_dal = models.DateField()

    class Meta:
        verbose_name_plural = 'Iva'

    
    
class Prodotto(models.Model):
    nome = models.CharField(max_length=255)
    descrizione = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Prodotti'

    
    
class Unita_misura(models.Model):
    nome = models.CharField(max_length=255)
    abbreviazione = models.CharField(max_length=16)
    
    class Meta:
        verbose_name_plural = 'Unità di misura'

    
    
# class Prezzo_um(models.Model):
#     prodotto = models.ForeignKey(Prodotto, related_name="prezzi_um")
#     cliente = models.ForeignKey(Cliente, related_name="prezzi_um")
#     unita_misura = models.ForeignKey(Unita_misura)
#     prezzo = models.DecimalField(decimal_places=2, max_digits=10)
#     attivo_dal = models.DateField()
    
    
class Fattura(models.Model):
    numero = models.IntegerField()
    data = models.DateField()

    class Meta:
        abstract = True


# class Fattura_vendita(Fattura):
#     cliente = models.ForeignKey(Cliente, related_name="fatture_vendita")
#     prodotto = models.ManyToManyField(Prodotto, related_name="fatture_vendita")
# 
# 
# class Riga_fattura_vendita(models.Model):
#     fattura = models.ForeignKey(Fattura_vendita, related_name="righe_fattura_vendita")
#     prodotto = models.ForeignKey(Prodotto, related_name="righe_fattura_vendita")


# class DocumentoTrasporto(models.Model):
#     numero = models.IntegerField()
#     data = models.DateField()
#     cliente = models.ForeignKey(Cliente)
#     prodotto = models.ManyToManyField(Prodotto)
# 
# 
# class Riga_ddt(models.Model):
#     ddt = models.ForeignKey(DocumentoTrasporto, related_name="righe_ddt")
#     prodotto = models.ForeignKey(Prodotto, related_name="righe_ddt")
#     prezzo = models.ForeignKey(Prezzo_um)
