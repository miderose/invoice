# -*- coding: utf-8 -*-
from django.forms.models import ModelForm
from acquisti.models import Fattura_acquisto, Fornitore, Riga_fattura_acquisto,\
    Prodotto, Unita_misura, DESTINAZIONE_CHOICES
from django import forms


class FatturaAcquistoAdminForm(ModelForm):
    fornitore = forms.CharField(label="Fornitore")#widget=forms.TextInput(attrs={'class':'special'}))
    numero = forms.CharField(label="Fattura nr.", required=False)
    totale = forms.DecimalField(label="Totale imponibile fattura", decimal_places=5, required=False)

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
            fornitore = Fornitore.objects.get(ragione_sociale=fornitore)
        return fornitore


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
    totale_riga = forms.DecimalField(label="Totale riga", decimal_places=5)

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
            self.initial['unita_di_misura'] = self.instance.unita_di_misura.nome
        except:
            pass
                
    def clean_prodotto(self):
        prodotto = self.cleaned_data['prodotto'].strip()
        prodotto = Prodotto.objects.get(nome=prodotto)
        
        return prodotto

    def clean_unita_di_misura(self):
        unita_di_misura = self.cleaned_data['unita_di_misura'].strip()
        unita_di_misura = Unita_misura.objects.get(nome=unita_di_misura)
        
        return unita_di_misura
