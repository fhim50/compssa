# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fileserver'
        db.create_table('fileserver_fileserver', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=220)),
        ))
        db.send_create_signal('fileserver', ['Fileserver'])


    def backwards(self, orm):
        # Deleting model 'Fileserver'
        db.delete_table('fileserver_fileserver')


    models = {
        'fileserver.fileserver': {
            'Meta': {'object_name': 'Fileserver'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '220'})
        }
    }

    complete_apps = ['fileserver']