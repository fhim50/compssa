# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Registration'
        db.create_table('registration', (
            ('ID', self.gf('django.db.models.fields.IntegerField')(max_length=8, primary_key=True)),
            ('sur_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('other_names', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('programe', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('phone_number', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('hall', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('room_number', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
        ))
        db.send_create_signal(u'register', ['Registration'])


    def backwards(self, orm):
        # Deleting model 'Registration'
        db.delete_table('registration')


    models = {
        u'register.registration': {
            'ID': ('django.db.models.fields.IntegerField', [], {'max_length': '8', 'primary_key': 'True'}),
            'Meta': {'object_name': 'Registration', 'db_table': "'registration'"},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'hall': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'other_names': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_number': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'programe': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'room_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'sur_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['register']