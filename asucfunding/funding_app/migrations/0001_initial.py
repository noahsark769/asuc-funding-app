# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Admin'
        db.create_table('funding_app_admin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('funding_app', ['Admin'])

        # Adding model 'FundingRequest'
        db.create_table('funding_app_fundingrequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.IntegerField')()),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('requestType', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('requestCategory', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('grantCategory', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('eventType', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('fundingRound', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('studentGroup', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('requestStatus', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('funding_app', ['FundingRequest'])

        # Adding model 'GraduateRequest'
        db.create_table('funding_app_graduaterequest', (
            ('fundingrequest_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['funding_app.FundingRequest'], unique=True, primary_key=True)),
            ('academicDepartmentalAffiliate', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('gaDelegate', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('studentOrgMemTot', self.gf('django.db.models.fields.IntegerField')()),
            ('studentOrgGrad', self.gf('django.db.models.fields.IntegerField')()),
            ('studentOrgUnd', self.gf('django.db.models.fields.IntegerField')()),
            ('attendedWaiver', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('funding_app', ['GraduateRequest'])

        # Adding model 'UndergraduateRequest'
        db.create_table('funding_app_undergraduaterequest', (
            ('fundingrequest_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['funding_app.FundingRequest'], unique=True, primary_key=True)),
            ('studentOrgTot', self.gf('django.db.models.fields.IntegerField')()),
            ('stduentOrgStud', self.gf('django.db.models.fields.IntegerField')()),
            ('attended', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('funding_app', ['UndergraduateRequest'])

        # Adding model 'TravelRequest'
        db.create_table('funding_app_travelrequest', (
            ('fundingrequest_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['funding_app.FundingRequest'], unique=True, primary_key=True)),
            ('requestingAs', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('funding_app', ['TravelRequest'])

        # Adding model 'Budget'
        db.create_table('funding_app_budget', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('additionalInfo', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('amountAwarded', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('totalRequestedAmount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('totalOtherFunding', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('requestedTotal', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('funding_app', ['Budget'])

        # Adding model 'ItemDescription'
        db.create_table('funding_app_itemdescription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('budget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funding_app.Budget'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('itemCost', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('requestedAmount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('otherFunding', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('total', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('funding_app', ['ItemDescription'])

        # Adding model 'Event'
        db.create_table('funding_app_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fundingRequest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funding_app.FundingRequest'])),
            ('eventTitle', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('sameBudgetForRecurringEvents', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('startDate', self.gf('django.db.models.fields.DateField')()),
            ('endDate', self.gf('django.db.models.fields.DateField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('waiverRequested', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('attendenceNonStudent', self.gf('django.db.models.fields.IntegerField')()),
            ('attendenceUnd', self.gf('django.db.models.fields.IntegerField')()),
            ('attendenceGrad', self.gf('django.db.models.fields.IntegerField')()),
            ('budget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funding_app.Budget'])),
        ))
        db.send_create_signal('funding_app', ['Event'])

        # Adding model 'TravelEvent'
        db.create_table('funding_app_travelevent', (
            ('event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['funding_app.Event'], unique=True, primary_key=True)),
            ('depatureDate', self.gf('django.db.models.fields.DateField')()),
            ('returnDate', self.gf('django.db.models.fields.DateField')()),
            ('presenting', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('presentationTitle', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('funding_app', ['TravelEvent'])

        # Adding model 'Config'
        db.create_table('funding_app_config', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('funding_app', ['Config'])

        # Adding model 'ConfigAdmin'
        db.create_table('funding_app_configadmin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('config', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funding_app.Config'])),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('funding_app', ['ConfigAdmin'])

        # Adding model 'ConfigLocation'
        db.create_table('funding_app_configlocation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('config', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funding_app.Config'])),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('funding_app', ['ConfigLocation'])

        # Adding model 'ConfigUGReqCat'
        db.create_table('funding_app_configugreqcat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('config', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funding_app.Config'])),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('funding_app', ['ConfigUGReqCat'])

        # Adding model 'ConfigGradReqCat'
        db.create_table('funding_app_configgradreqcat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('config', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funding_app.Config'])),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('funding_app', ['ConfigGradReqCat'])

        # Adding model 'ConfigUGGrant'
        db.create_table('funding_app_configuggrant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('config', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funding_app.Config'])),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('funding_app', ['ConfigUGGrant'])

        # Adding model 'ConfigGradGrant'
        db.create_table('funding_app_configgradgrant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('config', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funding_app.Config'])),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('funding_app', ['ConfigGradGrant'])

        # Adding model 'ConfigFundingRound'
        db.create_table('funding_app_configfundinground', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('config', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funding_app.Config'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('deadline', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('funding_app', ['ConfigFundingRound'])

        # Adding model 'ConfigGradDelegate'
        db.create_table('funding_app_configgraddelegate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('config', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['funding_app.Config'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('funding_app', ['ConfigGradDelegate'])


    def backwards(self, orm):
        # Deleting model 'Admin'
        db.delete_table('funding_app_admin')

        # Deleting model 'FundingRequest'
        db.delete_table('funding_app_fundingrequest')

        # Deleting model 'GraduateRequest'
        db.delete_table('funding_app_graduaterequest')

        # Deleting model 'UndergraduateRequest'
        db.delete_table('funding_app_undergraduaterequest')

        # Deleting model 'TravelRequest'
        db.delete_table('funding_app_travelrequest')

        # Deleting model 'Budget'
        db.delete_table('funding_app_budget')

        # Deleting model 'ItemDescription'
        db.delete_table('funding_app_itemdescription')

        # Deleting model 'Event'
        db.delete_table('funding_app_event')

        # Deleting model 'TravelEvent'
        db.delete_table('funding_app_travelevent')

        # Deleting model 'Config'
        db.delete_table('funding_app_config')

        # Deleting model 'ConfigAdmin'
        db.delete_table('funding_app_configadmin')

        # Deleting model 'ConfigLocation'
        db.delete_table('funding_app_configlocation')

        # Deleting model 'ConfigUGReqCat'
        db.delete_table('funding_app_configugreqcat')

        # Deleting model 'ConfigGradReqCat'
        db.delete_table('funding_app_configgradreqcat')

        # Deleting model 'ConfigUGGrant'
        db.delete_table('funding_app_configuggrant')

        # Deleting model 'ConfigGradGrant'
        db.delete_table('funding_app_configgradgrant')

        # Deleting model 'ConfigFundingRound'
        db.delete_table('funding_app_configfundinground')

        # Deleting model 'ConfigGradDelegate'
        db.delete_table('funding_app_configgraddelegate')


    models = {
        'funding_app.admin': {
            'Meta': {'object_name': 'Admin'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'funding_app.budget': {
            'Meta': {'object_name': 'Budget'},
            'additionalInfo': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'amountAwarded': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'requestedTotal': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'totalOtherFunding': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'totalRequestedAmount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        'funding_app.config': {
            'Meta': {'object_name': 'Config'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funding_app.configadmin': {
            'Meta': {'object_name': 'ConfigAdmin'},
            'config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Config']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funding_app.configfundinground': {
            'Meta': {'object_name': 'ConfigFundingRound'},
            'config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Config']"}),
            'deadline': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'funding_app.configgraddelegate': {
            'Meta': {'object_name': 'ConfigGradDelegate'},
            'config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Config']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'funding_app.configgradgrant': {
            'Meta': {'object_name': 'ConfigGradGrant'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Config']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funding_app.configgradreqcat': {
            'Meta': {'object_name': 'ConfigGradReqCat'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Config']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funding_app.configlocation': {
            'Meta': {'object_name': 'ConfigLocation'},
            'config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Config']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'funding_app.configuggrant': {
            'Meta': {'object_name': 'ConfigUGGrant'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Config']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funding_app.configugreqcat': {
            'Meta': {'object_name': 'ConfigUGReqCat'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Config']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funding_app.event': {
            'Meta': {'object_name': 'Event'},
            'attendenceGrad': ('django.db.models.fields.IntegerField', [], {}),
            'attendenceNonStudent': ('django.db.models.fields.IntegerField', [], {}),
            'attendenceUnd': ('django.db.models.fields.IntegerField', [], {}),
            'budget': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Budget']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'endDate': ('django.db.models.fields.DateField', [], {}),
            'eventTitle': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'fundingRequest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.FundingRequest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sameBudgetForRecurringEvents': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'startDate': ('django.db.models.fields.DateField', [], {}),
            'waiverRequested': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'funding_app.fundingrequest': {
            'Meta': {'object_name': 'FundingRequest'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'eventType': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'fundingRound': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'grantCategory': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'requestCategory': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'requestStatus': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'requestType': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'studentGroup': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'uid': ('django.db.models.fields.IntegerField', [], {})
        },
        'funding_app.graduaterequest': {
            'Meta': {'object_name': 'GraduateRequest', '_ormbases': ['funding_app.FundingRequest']},
            'academicDepartmentalAffiliate': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'attendedWaiver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fundingrequest_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['funding_app.FundingRequest']", 'unique': 'True', 'primary_key': 'True'}),
            'gaDelegate': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'studentOrgGrad': ('django.db.models.fields.IntegerField', [], {}),
            'studentOrgMemTot': ('django.db.models.fields.IntegerField', [], {}),
            'studentOrgUnd': ('django.db.models.fields.IntegerField', [], {})
        },
        'funding_app.itemdescription': {
            'Meta': {'object_name': 'ItemDescription'},
            'budget': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Budget']"}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemCost': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'otherFunding': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'requestedAmount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        'funding_app.travelevent': {
            'Meta': {'object_name': 'TravelEvent', '_ormbases': ['funding_app.Event']},
            'depatureDate': ('django.db.models.fields.DateField', [], {}),
            'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['funding_app.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'presentationTitle': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'presenting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'returnDate': ('django.db.models.fields.DateField', [], {})
        },
        'funding_app.travelrequest': {
            'Meta': {'object_name': 'TravelRequest', '_ormbases': ['funding_app.FundingRequest']},
            'fundingrequest_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['funding_app.FundingRequest']", 'unique': 'True', 'primary_key': 'True'}),
            'requestingAs': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'funding_app.undergraduaterequest': {
            'Meta': {'object_name': 'UndergraduateRequest', '_ormbases': ['funding_app.FundingRequest']},
            'attended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fundingrequest_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['funding_app.FundingRequest']", 'unique': 'True', 'primary_key': 'True'}),
            'stduentOrgStud': ('django.db.models.fields.IntegerField', [], {}),
            'studentOrgTot': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['funding_app']