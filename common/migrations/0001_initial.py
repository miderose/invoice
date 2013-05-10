# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gruppo_orientativo_iva'
        db.create_table(u'common_gruppo_orientativo_iva', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome_gruppo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('aliquota_orientativa', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'common', ['Gruppo_orientativo_iva'])

        # Adding model 'Iva'
        db.create_table(u'common_iva', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gruppo_orientativo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['common.Gruppo_orientativo_iva'])),
            ('percentuale_aliquota', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('etichetta', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('attiva_dal', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'common', ['Iva'])

        # Adding model 'Prodotto'
        db.create_table(u'common_prodotto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('descrizione', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'common', ['Prodotto'])

        # Adding model 'Unita_misura'
        db.create_table(u'common_unita_misura', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abbreviazione', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'common', ['Unita_misura'])


    def backwards(self, orm):
        # Deleting model 'Gruppo_orientativo_iva'
        db.delete_table(u'common_gruppo_orientativo_iva')

        # Deleting model 'Iva'
        db.delete_table(u'common_iva')

        # Deleting model 'Prodotto'
        db.delete_table(u'common_prodotto')

        # Deleting model 'Unita_misura'
        db.delete_table(u'common_unita_misura')


    models = {
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

    complete_apps = ['common']