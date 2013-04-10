# -*- coding: utf-8 -*-
from django.contrib import admin
from acquisti.models import Riga_fattura_acquisto, Fornitore,\
    Gruppo_orientativo_iva, Iva, Prodotto, Unita_misura, Fattura_acquisto,\
    Categoria_StudiSett

class Riga_fattura_acquisto_inline(admin.TabularInline):
    model = Riga_fattura_acquisto
    extra = 5



class ClienteAdmin(admin.ModelAdmin):
    pass

class FornitoreAdmin(admin.ModelAdmin):
    pass

class Gruppo_orientativo_ivaAdmin(admin.ModelAdmin):
    pass

class IvaAdmin(admin.ModelAdmin):
    pass

class ProdottoAdmin(admin.ModelAdmin):
    pass

class Unita_misuraAdmin(admin.ModelAdmin):
    pass

class Prezzo_umAdmin(admin.ModelAdmin):
    pass

class Fattura_acquistoAdmin(admin.ModelAdmin):
    fields = ('fornitore', ('numero', 'data'))
    inlines = [Riga_fattura_acquisto_inline]


class Fattura_venditaAdmin(admin.ModelAdmin):
    pass

class Riga_fattura_acquistoAdmin(admin.ModelAdmin):
    pass

class Riga_fattura_venditaAdmin(admin.ModelAdmin):
    pass

class DocumentoTrasportoAdmin(admin.ModelAdmin):
    pass

class Riga_ddtAdmin(admin.ModelAdmin):
    pass


class Categoria_StudiSettAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Fornitore, FornitoreAdmin)
admin.site.register(Gruppo_orientativo_iva, Gruppo_orientativo_ivaAdmin)
admin.site.register(Iva, IvaAdmin)
admin.site.register(Prodotto, ProdottoAdmin)
admin.site.register(Unita_misura, Unita_misuraAdmin)
# admin.site.register(Prezzo_um, Prezzo_umAdmin)
admin.site.register(Fattura_acquisto, Fattura_acquistoAdmin)
# admin.site.register(Fattura_vendita, Fattura_venditaAdmin)
admin.site.register(Riga_fattura_acquisto, Riga_fattura_acquistoAdmin)
# admin.site.register(Riga_fattura_vendita, Riga_fattura_venditaAdmin)
# admin.site.register(DocumentoTrasporto, DocumentoTrasportoAdmin)
# admin.site.register(Riga_ddt, Riga_ddtAdmin)
admin.site.register(Categoria_StudiSett, Categoria_StudiSettAdmin)







































