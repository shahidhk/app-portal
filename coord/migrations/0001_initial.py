# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Answer'
        db.create_table('coord_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Question'], null=True)),
            ('answer', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('coord', ['Answer'])

        # Adding model 'Credential'
        db.create_table('coord_credential', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('coord', ['Credential'])

        # Adding model 'Reference'
        db.create_table('coord_reference', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('coord', ['Reference'])

        # Adding model 'Application'
        db.create_table('coord_application', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('subdept', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.SubDept'])),
            ('preference', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('credentials', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coord.Credential'])),
            ('references', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['coord.Reference'])),
            ('lockstatus', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('status', self.gf('django.db.models.fields.CharField')(default='pending', max_length='10')),
        ))
        db.send_create_signal('coord', ['Application'])

        # Adding M2M table for field answers on 'Application'
        m2m_table_name = db.shorten_name('coord_application_answers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('application', models.ForeignKey(orm['coord.application'], null=False)),
            ('answer', models.ForeignKey(orm['coord.answer'], null=False))
        ))
        db.create_unique(m2m_table_name, ['application_id', 'answer_id'])


    def backwards(self, orm):
        # Deleting model 'Answer'
        db.delete_table('coord_answer')

        # Deleting model 'Credential'
        db.delete_table('coord_credential')

        # Deleting model 'Reference'
        db.delete_table('coord_reference')

        # Deleting model 'Application'
        db.delete_table('coord_application')

        # Removing M2M table for field answers on 'Application'
        db.delete_table(db.shorten_name('coord_application_answers'))


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

    complete_apps = ['coord']