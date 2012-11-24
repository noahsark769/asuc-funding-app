# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'GraduateRequest.studentOrgMemTot'
        db.delete_column('funding_app_graduaterequest', 'studentOrgMemTot')

        # Deleting field 'GraduateRequest.studentOrgUnd'
        db.delete_column('funding_app_graduaterequest', 'studentOrgUnd')

        # Adding field 'GraduateRequest.studentOrgTot'
        db.add_column('funding_app_graduaterequest', 'studentOrgTot',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'GraduateRequest.studentOrgUG'
        db.add_column('funding_app_graduaterequest', 'studentOrgUG',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FundingRequest.contingency'
        db.add_column('funding_app_fundingrequest', 'contingency',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'FundingRequest.eventTitle'
        db.add_column('funding_app_fundingrequest', 'eventTitle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'FundingRequest.description'
        db.add_column('funding_app_fundingrequest', 'description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=5000),
                      keep_default=False)

        # Deleting field 'Event.eventTitle'
        db.delete_column('funding_app_event', 'eventTitle')

        # Deleting field 'Event.description'
        db.delete_column('funding_app_event', 'description')

        # Deleting field 'Event.attendenceUnd'
        db.delete_column('funding_app_event', 'attendenceUnd')

        # Adding field 'Event.attendenceUG'
        db.add_column('funding_app_event', 'attendenceUG',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'UndergraduateRequest.stduentOrgStud'
        db.delete_column('funding_app_undergraduaterequest', 'stduentOrgStud')

        # Adding field 'UndergraduateRequest.studentOrgStud'
        db.add_column('funding_app_undergraduaterequest', 'studentOrgStud',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'GraduateRequest.studentOrgMemTot'
        db.add_column('funding_app_graduaterequest', 'studentOrgMemTot',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'GraduateRequest.studentOrgUnd'
        db.add_column('funding_app_graduaterequest', 'studentOrgUnd',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'GraduateRequest.studentOrgTot'
        db.delete_column('funding_app_graduaterequest', 'studentOrgTot')

        # Deleting field 'GraduateRequest.studentOrgUG'
        db.delete_column('funding_app_graduaterequest', 'studentOrgUG')

        # Deleting field 'FundingRequest.contingency'
        db.delete_column('funding_app_fundingrequest', 'contingency')

        # Deleting field 'FundingRequest.eventTitle'
        db.delete_column('funding_app_fundingrequest', 'eventTitle')

        # Deleting field 'FundingRequest.description'
        db.delete_column('funding_app_fundingrequest', 'description')

        # Adding field 'Event.eventTitle'
        db.add_column('funding_app_event', 'eventTitle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Event.description'
        db.add_column('funding_app_event', 'description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=5000),
                      keep_default=False)

        # Adding field 'Event.attendenceUnd'
        db.add_column('funding_app_event', 'attendenceUnd',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Event.attendenceUG'
        db.delete_column('funding_app_event', 'attendenceUG')

        # Adding field 'UndergraduateRequest.stduentOrgStud'
        db.add_column('funding_app_undergraduaterequest', 'stduentOrgStud',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'UndergraduateRequest.studentOrgStud'
        db.delete_column('funding_app_undergraduaterequest', 'studentOrgStud')


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
        'funding_app.configadmin': {
            'Meta': {'object_name': 'ConfigAdmin'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funding_app.configfundinground': {
            'Meta': {'object_name': 'ConfigFundingRound'},
            'deadline': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'funding_app.configgraddelegate': {
            'Meta': {'object_name': 'ConfigGradDelegate'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'funding_app.configgradgrant': {
            'Meta': {'object_name': 'ConfigGradGrant'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funding_app.configgradreqcat': {
            'Meta': {'object_name': 'ConfigGradReqCat'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funding_app.configlocation': {
            'Meta': {'object_name': 'ConfigLocation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'funding_app.configuggrant': {
            'Meta': {'object_name': 'ConfigUGGrant'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funding_app.configugreqcat': {
            'Meta': {'object_name': 'ConfigUGReqCat'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'funding_app.event': {
            'Meta': {'object_name': 'Event'},
            'attendenceGrad': ('django.db.models.fields.IntegerField', [], {}),
            'attendenceNonStudent': ('django.db.models.fields.IntegerField', [], {}),
            'attendenceUG': ('django.db.models.fields.IntegerField', [], {}),
            'budget': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.Budget']"}),
            'endDate': ('django.db.models.fields.DateField', [], {}),
            'fundingRequest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['funding_app.FundingRequest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sameBudgetForRecurringEvents': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'startDate': ('django.db.models.fields.DateField', [], {}),
            'waiverRequested': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'funding_app.fundingrequest': {
            'Meta': {'object_name': 'FundingRequest'},
            'contingency': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dateSubmitted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'eventTitle': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
            'studentOrgTot': ('django.db.models.fields.IntegerField', [], {}),
            'studentOrgUG': ('django.db.models.fields.IntegerField', [], {})
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
            'studentOrgStud': ('django.db.models.fields.IntegerField', [], {}),
            'studentOrgTot': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['funding_app']