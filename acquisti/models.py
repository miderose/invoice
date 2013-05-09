# -*- coding: utf-8 -*-

from django.db import models
from common.models import Anagrafica, Gruppo_orientativo_iva, Iva, Prodotto,\
    Unita_misura

DESTINAZIONE_CHOICES = (("Pasticceria", "Pasticceria"),
                        ("Bar", "Bar"))


class Fornitore(Anagrafica):
    class Meta:
        verbose_name_plural = 'Fornitori'
        ordering = ("ragione_sociale",)
        
    def __unicode__(self):
        return self.ragione_sociale



class Gruppo_orientativo_iva(Gruppo_orientativo_iva):
    class Meta:
        verbose_name_plural = 'Gruppi orientativi IVA'
    
    
class Iva(Iva):
    class Meta:
        verbose_name_plural = 'Iva'
    

class Categoria_StudiSett(models.Model):
    nome = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Categorie StudiDiSettore'
        verbose_name = 'Categoria StudiDiSettore'
        
    def __unicode__(self):
        return self.nome


class Prodotto(Prodotto):
    destinazione = models.CharField(max_length=32, choices=DESTINAZIONE_CHOICES, default="Pasticceria")
    categoria_studi_sett = models.ManyToManyField(Categoria_StudiSett)
    
    class Meta:
        verbose_name_plural = 'Prodotti'
    
    def __unicode__(self):
        return self.nome

    
class Unita_misura(Unita_misura):
    class Meta:
        verbose_name_plural = 'Unità di misura'

    def __unicode__(self):
        return self.nome

    
class Fattura_acquisto(models.Model):
    fornitore = models.ForeignKey(Fornitore, related_name="fatture_acquisto")
    numero = models.IntegerField(blank=True, null=True)
    prodotto = models.ManyToManyField(Prodotto, related_name="fatture_acquisto", through="Riga_fattura_acquisto")
    data = models.DateField()
    da_rivedere = models.BooleanField(default=False)
    note = models.TextField(null=True, blank=True)
    totale = 0.0
    
    class Meta:
        verbose_name_plural = 'Fatture di acquisto'

    def __unicode__(self):
        return "%s - %s" % (self.fornitore, self.data.strftime("%d/%m/%Y"))
    
    def get_totale(self):
        totale = 0.0 #convertire in decimal
        for riga in self.righe_fattura_acquisto.all():
            totale += riga.get_totale()
        
        return totale


class Riga_fattura_acquisto(models.Model):
    fattura = models.ForeignKey(Fattura_acquisto, related_name="righe_fattura_acquisto")
    prodotto = models.ForeignKey(Prodotto, related_name="righe_fattura_acquisto")
    prezzo = models.DecimalField(decimal_places=2, max_digits=10)
    unita_di_misura = models.ForeignKey(Unita_misura)
    quantita = models.FloatField()
    da_rivedere = models.BooleanField(default=False)
    totale = 0.0
    
    class Meta:
        verbose_name_plural = 'Righe fatture di acquisto'

    def __unicode__(self):
        return "Riga:"
    
    def get_totale(self):
        return self.prezzo * self.quantita
