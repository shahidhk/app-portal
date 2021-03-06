# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SubDept'
        db.create_table('core_subdept', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dept', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('impose_cgpa', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('close_apps', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['SubDept'])

        # Adding model 'Question'
        db.create_table('core_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subdept', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.SubDept'])),
            ('question', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Question'])

        # Adding model 'Comments'
        db.create_table('core_comments', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('answer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coord.Answer'])),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('core', ['Comments'])

        # Adding model 'AppComments'
        db.create_table('core_appcomments', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coord.Application'], unique=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('core', ['AppComments'])

        # Adding model 'Instructions'
        db.create_table('core_instructions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sub_dept', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.SubDept'], unique=True, null=True)),
            ('instructions', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('core', ['Instructions'])


    def backwards(self, orm):
        # Deleting model 'SubDept'
        db.delete_table('core_subdept')

        # Deleting model 'Question'
        db.delete_table('core_question')

        # Deleting model 'Comments'
        db.delete_table('core_comments')

        # Deleting model 'AppComments'
        db.delete_table('core_appcomments')

        # Deleting model 'Instructions'
        db.delete_table('core_instructions')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'coord.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Question']", 'null': 'True'})
        },
        'coord.application': {
            'Meta': {'object_name': 'Application'},
            'answers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['coord.Answer']", 'symmetrical': 'False'}),
            'credentials': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coord.Credential']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lockstatus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'preference': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'references': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coord.Reference']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': "'10'"}),
            'subdept': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.SubDept']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'coord.credential': {
            'Meta': {'object_name': 'Credential'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'coord.reference': {
            'Meta': {'object_name': 'Reference'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'core.appcomments': {
            'Meta': {'object_name': 'AppComments'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coord.Application']", 'unique': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'core.comments': {
            'Meta': {'object_name': 'Comments'},
            'answer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['coord.Answer']"}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'core.instructions': {
            'Meta': {'object_name': 'Instructions'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sub_dept': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.SubDept']", 'unique': 'True', 'null': 'True'})
        },
        'core.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'subdept': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.SubDept']"})
        },
        'core.subdept': {
            'Meta': {'object_name': 'SubDept'},
            'close_apps': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dept': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impose_cgpa': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['core']