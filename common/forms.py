# -*- coding: utf-8 -*-
from django import forms
from django.forms.models import ModelForm

from acquisti.models import Fattura_acquisto, Fornitore, Riga_fattura_acquisto,\
    Prodotto, Unita_misura, DESTINAZIONE_CHOICES

DATE_FORMATS = ["%d/%m/%y", # 29/09/84
                "%d/%m/%Y", # 29/09/1984
                "%d%m%y",   # 290984
                "%d%m%Y",   # 29091984
               ]


class FatturaAcquistoAdminForm(ModelForm):
    fornitore = forms.CharField(label="Fornitore")#widget=forms.TextInput(attrs={'class':'special'}))
    numero = forms.CharField(label="Fattura nr.", required=False)
    totale = forms.DecimalField(label="Totale imponibile fattura", decimal_places=5, required=False)
    data = forms.DateField(label="Data fattura", input_formats=DATE_FORMATS)

    class Meta:
        model = Fattura_acquisto
        
    def __init__(self, *args, **kwargs):
        super(FatturaAcquistoAdminForm, self).__init__(*args, **kwargs)
        
        try:
            self.initial['fornitore'] = self.instance.fornitore.ragione_sociale
        except:
            pass
        
    def clean_fornitore(self):
        fornitore = self.cleaned_data['fornitore'].strip()
        if fornitore.isdigit():
            fornitore = Fornitore.objects.get(id=fornitore)
        else:
            try:
                fornitore = Fornitore.objects.get(ragione_sociale__icontains=fornitore)
            except Fornitore.DoesNotExist:
                raise forms.ValidationError('Il fornitore "%s" non esiste. Devi crearlo.' % fornitore)
        return fornitore

    def clean_numero(self):
        numero = self.cleaned_data['numero'].strip()
        if len(numero) < 1:
            numero = None
        return numero        


class ProdottoAdminForm(ModelForm):
    destinazione = forms.ChoiceField(widget=forms.RadioSelect(), label="destinazione", choices=DESTINAZIONE_CHOICES)
    class Meta:
        model = Prodotto
        
    def __init__(self, *args, **kwargs):
        super(ProdottoAdminForm, self).__init__(*args, **kwargs)
        self.initial['destinazione'] = "Pasticceria"


class RigaFatturaAcquistoAdminForm(ModelForm):
    prodotto = forms.CharField(label="Prodotto")
    unita_di_misura = forms.CharField(label="Unità di misura")
    prezzo = forms.CharField(label="Prezzo unitario")
    quantita = forms.CharField(label="Quantita")
    totale_riga = forms.DecimalField(label="Totale riga", decimal_places=5, required=False)

    class Meta:
        model = Riga_fattura_acquisto
        
    def __init__(self, *args, **kwargs):
        super(RigaFatturaAcquistoAdminForm, self).__init__(*args, **kwargs)
        self.initial['destinazione'] = "Pasticceria"
        
        try:
            self.initial['prodotto'] = self.instance.prodotto.nome
        except:
            pass
        
        try:
            self.initial['unita_di_misura'] = self.instance.unita_di_misura.abbreviazione
        except:
            pass
                
    def clean_prodotto(self):
        prodotto = self.cleaned_data['prodotto'].strip()
        try:
            prodotto = Prodotto.objects.get(nome__icontains=prodotto)
        except Prodotto.DoesNotExist:
            raise forms.ValidationError('Il prodotto "%s" non esiste. Devi crearlo.' % prodotto)
        return prodotto

    def clean_prezzo(self):
        prezzo = self.cleaned_data['prezzo'].strip()
        return float(prezzo.replace(",", "."))

    def clean_quantita(self):
        quantita = self.cleaned_data['quantita'].strip()
        return float(quantita.replace(",", "."))

    def clean_unita_di_misura(self):
        unita_di_misura = self.cleaned_data['unita_di_misura'].strip()
        try:
            unita_di_misura = Unita_misura.objects.get(abbreviazione__iexact=unita_di_misura)
        except Unita_misura.DoesNotExist:
            try:
                unita_di_misura = Unita_misura.objects.get(nome__iexact=unita_di_misura)
            except Unita_misura.DoesNotExist:
                raise forms.ValidationError('L\'unita\' di misura "%s" non esiste. Devi crearla.' % unita_di_misura)
        
        return unita_di_misura
