# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Budget.comment'
        db.alter_column('funding_app_budget', 'comment', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Budget.additionalInfo'
        db.alter_column('funding_app_budget', 'additionalInfo', self.gf('django.db.models.fields.CharField')(max_length=5000))

        # Changing field 'ConfigUGReqCat.category'
        db.alter_column('funding_app_configugreqcat', 'category', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Admin.uid'
        db.alter_column('funding_app_admin', 'uid', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Admin.email'
        db.alter_column('funding_app_admin', 'email', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'ConfigUGGrant.category'
        db.alter_column('funding_app_configuggrant', 'category', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'ConfigGradDelegate.email'
        db.alter_column('funding_app_configgraddelegate', 'email', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'ConfigGradDelegate.name'
        db.alter_column('funding_app_configgraddelegate', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'ItemDescription.comment'
        db.alter_column('funding_app_itemdescription', 'comment', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'ItemDescription.description'
        db.alter_column('funding_app_itemdescription', 'description', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'ConfigAdmin.email'
        db.alter_column('funding_app_configadmin', 'email', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'TravelEvent.presentationTitle'
        db.alter_column('funding_app_travelevent', 'presentationTitle', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'ConfigGradReqCat.category'
        db.alter_column('funding_app_configgradreqcat', 'category', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'ConfigLocation.location'
        db.alter_column('funding_app_configlocation', 'location', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'GraduateRequest.academicDepartmentalAffiliate'
        db.alter_column('funding_app_graduaterequest', 'academicDepartmentalAffiliate', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'GraduateRequest.gaDelegate'
        db.alter_column('funding_app_graduaterequest', 'gaDelegate', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'ConfigFundingRound.name'
        db.alter_column('funding_app_configfundinground', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))
        # Adding field 'FundingRequest.name'
        db.add_column('funding_app_fundingrequest', 'name',
                      self.gf('django.db.models.fields.CharField')(default='Shitface Mcgee', max_length=50),
                      keep_default=False)


        # Changing field 'FundingRequest.fundingRound'
        db.alter_column('funding_app_fundingrequest', 'fundingRound', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'FundingRequest.grantCategory'
        db.alter_column('funding_app_fundingrequest', 'grantCategory', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'FundingRequest.requestType'
        db.alter_column('funding_app_fundingrequest', 'requestType', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'FundingRequest.eventType'
        db.alter_column('funding_app_fundingrequest', 'eventType', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'FundingRequest.requestCategory'
        db.alter_column('funding_app_fundingrequest', 'requestCategory', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'FundingRequest.studentGroup'
        db.alter_column('funding_app_fundingrequest', 'studentGroup', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'FundingRequest.requestStatus'
        db.alter_column('funding_app_fundingrequest', 'requestStatus', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'FundingRequest.email'
        db.alter_column('funding_app_fundingrequest', 'email', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'ConfigGradGrant.category'
        db.alter_column('funding_app_configgradgrant', 'category', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'TravelRequest.requestingAs'
        db.alter_column('funding_app_travelrequest', 'requestingAs', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Event.eventTitle'
        db.alter_column('funding_app_event', 'eventTitle', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Event.description'
        db.alter_column('funding_app_event', 'description', self.gf('django.db.models.fields.CharField')(max_length=5000))

        # Changing field 'Event.location'
        db.alter_column('funding_app_event', 'location', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Budget.comment'
        db.alter_column('funding_app_budget', 'comment', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Budget.additionalInfo'
        db.alter_column('funding_app_budget', 'additionalInfo', self.gf('django.db.models.fields.CharField')(max_length=2000))

        # Changing field 'ConfigUGReqCat.category'
        db.alter_column('funding_app_configugreqcat', 'category', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Admin.uid'
        db.alter_column('funding_app_admin', 'uid', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Admin.email'
        db.alter_column('funding_app_admin', 'email', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'ConfigUGGrant.category'
        db.alter_column('funding_app_configuggrant', 'category', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'ConfigGradDelegate.email'
        db.alter_column('funding_app_configgraddelegate', 'email', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'ConfigGradDelegate.name'
        db.alter_column('funding_app_configgraddelegate', 'name', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'ItemDescription.comment'
        db.alter_column('funding_app_itemdescription', 'comment', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'ItemDescription.description'
        db.alter_column('funding_app_itemdescription', 'description', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'ConfigAdmin.email'
        db.alter_column('funding_app_configadmin', 'email', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'TravelEvent.presentationTitle'
        db.alter_column('funding_app_travelevent', 'presentationTitle', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'ConfigGradReqCat.category'
        db.alter_column('funding_app_configgradreqcat', 'category', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'ConfigLocation.location'
        db.alter_column('funding_app_configlocation', 'location', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'GraduateRequest.academicDepartmentalAffiliate'
        db.alter_column('funding_app_graduaterequest', 'academicDepartmentalAffiliate', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'GraduateRequest.gaDelegate'
        db.alter_column('funding_app_graduaterequest', 'gaDelegate', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'ConfigFundingRound.name'
        db.alter_column('funding_app_configfundinground', 'name', self.gf('django.db.models.fields.CharField')(max_length=30))
        # Deleting field 'FundingRequest.name'
        db.delete_column('funding_app_fundingrequest', 'name')


        # Changing field 'FundingRequest.fundingRound'
        db.alter_column('funding_app_fundingrequest', 'fundingRound', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'FundingRequest.grantCategory'
        db.alter_column('funding_app_fundingrequest', 'grantCategory', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'FundingRequest.requestType'
        db.alter_column('funding_app_fundingrequest', 'requestType', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'FundingRequest.eventType'
        db.alter_column('funding_app_fundingrequest', 'eventType', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'FundingRequest.requestCategory'
        db.alter_column('funding_app_fundingrequest', 'requestCategory', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'FundingRequest.studentGroup'
        db.alter_column('funding_app_fundingrequest', 'studentGroup', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'FundingRequest.requestStatus'
        db.alter_column('funding_app_fundingrequest', 'requestStatus', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'FundingRequest.email'
        db.alter_column('funding_app_fundingrequest', 'email', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'ConfigGradGrant.category'
        db.alter_column('funding_app_configgradgrant', 'category', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'TravelRequest.requestingAs'
        db.alter_column('funding_app_travelrequest', 'requestingAs', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Event.eventTitle'
        db.alter_column('funding_app_event', 'eventTitle', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Event.description'
        db.alter_column('funding_app_event', 'description', self.gf('django.db.models.fields.CharField')(max_length=2000))

        # Changing field 'Event.location'
        db.alter_column('funding_app_event', 'location', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        'funding_app.admin': {
            'Meta': {'object_name': 'Admin'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uid': ('django.db.models.fields.IntegerField', [], {})
        },
        'funding_app.budget': {
            'Meta': {'object_name': 'Budget'},
            'additionalInfo': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'amountAwarded': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
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
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funding_app.configfundinground': {
            'Meta': {'object_name': 'ConfigFundingRound'},
            'config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Config']"}),
            'deadline': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'funding_app.configgraddelegate': {
            'Meta': {'object_name': 'ConfigGradDelegate'},
            'config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Config']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'funding_app.configgradgrant': {
            'Meta': {'object_name': 'ConfigGradGrant'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Config']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funding_app.configgradreqcat': {
            'Meta': {'object_name': 'ConfigGradReqCat'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Config']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funding_app.configlocation': {
            'Meta': {'object_name': 'ConfigLocation'},
            'config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Config']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'funding_app.configuggrant': {
            'Meta': {'object_name': 'ConfigUGGrant'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Config']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funding_app.configugreqcat': {
            'Meta': {'object_name': 'ConfigUGReqCat'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Config']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funding_app.event': {
            'Meta': {'object_name': 'Event'},
            'attendenceGrad': ('django.db.models.fields.IntegerField', [], {}),
            'attendenceNonStudent': ('django.db.models.fields.IntegerField', [], {}),
            'attendenceUnd': ('django.db.models.fields.IntegerField', [], {}),
            'budget': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Budget']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'endDate': ('django.db.models.fields.DateField', [], {}),
            'eventTitle': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fundingRequest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.FundingRequest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sameBudgetForRecurringEvents': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'startDate': ('django.db.models.fields.DateField', [], {}),
            'waiverRequested': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'funding_app.fundingrequest': {
            'Meta': {'object_name': 'FundingRequest'},
            'dateSubmitted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'eventType': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fundingRound': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'grantCategory': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'requestCategory': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'requestStatus': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'requestType': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'studentGroup': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uid': ('django.db.models.fields.IntegerField', [], {})
        },
        'funding_app.graduaterequest': {
            'Meta': {'object_name': 'GraduateRequest', '_ormbases': ['funding_app.FundingRequest']},
            'academicDepartmentalAffiliate': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'attendedWaiver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fundingrequest_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['funding_app.FundingRequest']", 'unique': 'True', 'primary_key': 'True'}),
            'gaDelegate': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'studentOrgGrad': ('django.db.models.fields.IntegerField', [], {}),
            'studentOrgMemTot': ('django.db.models.fields.IntegerField', [], {}),
            'studentOrgUnd': ('django.db.models.fields.IntegerField', [], {})
        },
        'funding_app.itemdescription': {
            'Meta': {'object_name': 'ItemDescription'},
            'budget': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Budget']"}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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
            'presentationTitle': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'presenting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'returnDate': ('django.db.models.fields.DateField', [], {})
        },
        'funding_app.travelrequest': {
            'Meta': {'object_name': 'TravelRequest', '_ormbases': ['funding_app.FundingRequest']},
            'fundingrequest_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['funding_app.FundingRequest']", 'unique': 'True', 'primary_key': 'True'}),
            'requestingAs': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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