# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Registration.remarks'
        db.add_column('registration', 'remarks',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=300, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Registration.remarks'
        db.delete_column('registration', 'remarks')


    models = {
        u'register.registration': {
            'ID': ('django.db.models.fields.IntegerField', [], {'max_length': '8', 'primary_key': 'True'}),
            'Meta': {'object_name': 'Registration', 'db_table': "'registration'"},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'hall': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'other_names': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_number': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'programe': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'room_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'sur_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['register']