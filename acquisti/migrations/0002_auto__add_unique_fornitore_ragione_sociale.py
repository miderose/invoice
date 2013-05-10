# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Fornitore', fields ['ragione_sociale']
        db.create_unique(u'acquisti_fornitore', ['ragione_sociale'])


    def backwards(self, orm):
        # Removing unique constraint on 'Fornitore', fields ['ragione_sociale']
        db.delete_unique(u'acquisti_fornitore', ['ragione_sociale'])


    models = {
        u'acquisti.categoria_studisett': {
            'Meta': {'object_name': 'Categoria_StudiSett'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'acquisti.fattura_acquisto': {
            'Meta': {'object_name': 'Fattura_acquisto'},
            'da_rivedere': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data': ('django.db.models.fields.DateField', [], {}),
            'fornitore': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fatture_acquisto'", 'to': u"orm['acquisti.Fornitore']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'prodotto': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'fatture_acquisto'", 'symmetrical': 'False', 'through': u"orm['acquisti.Riga_fattura_acquisto']", 'to': u"orm['acquisti.Prodotto']"})
        },
        u'acquisti.fornitore': {
            'Meta': {'ordering': "('ragione_sociale',)", 'object_name': 'Fornitore'},
            'codice_fiscale': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'comune': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indirizzo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'partita_iva': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'ragione_sociale': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'referente': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tel_referente': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'acquisti.gruppo_orientativo_iva': {
            'Meta': {'object_name': 'Gruppo_orientativo_iva', '_ormbases': [u'common.Gruppo_orientativo_iva']},
            u'gruppo_orientativo_iva_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['common.Gruppo_orientativo_iva']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'acquisti.iva': {
            'Meta': {'object_name': 'Iva', '_ormbases': [u'common.Iva']},
            u'iva_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['common.Iva']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'acquisti.prodotto': {
            'Meta': {'object_name': 'Prodotto', '_ormbases': [u'common.Prodotto']},
            'categoria_studi_sett': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['acquisti.Categoria_StudiSett']", 'symmetrical': 'False'}),
            'destinazione': ('django.db.models.fields.CharField', [], {'default': "'Pasticceria'", 'max_length': '32'}),
            u'prodotto_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['common.Prodotto']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'acquisti.riga_fattura_acquisto': {
            'Meta': {'object_name': 'Riga_fattura_acquisto'},
            'da_rivedere': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fattura': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'righe_fattura_acquisto'", 'to': u"orm['acquisti.Fattura_acquisto']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prezzo': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'prodotto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'righe_fattura_acquisto'", 'to': u"orm['acquisti.Prodotto']"}),
            'quantita': ('django.db.models.fields.FloatField', [], {}),
            'unita_di_misura': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['acquisti.Unita_misura']"})
        },
        u'acquisti.unita_misura': {
            'Meta': {'object_name': 'Unita_misura', '_ormbases': [u'common.Unita_misura']},
            u'unita_misura_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['common.Unita_misura']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'common.gruppo_orientativo_iva': {
            'Meta': {'object_name': 'Gruppo_orientativo_iva'},
            'aliquota_orientativa': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome_gruppo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'common.iva': {
            'Meta': {'object_name': 'Iva'},
            'attiva_dal': ('django.db.models.fields.DateField', [], {}),
            'etichetta': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gruppo_orientativo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.Gruppo_orientativo_iva']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentuale_aliquota': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'common.prodotto': {
            'Meta': {'object_name': 'Prodotto'},
            'descrizione': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'common.unita_misura': {
            'Meta': {'object_name': 'Unita_misura'},
            'abbreviazione': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['acquisti']