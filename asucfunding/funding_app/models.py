from django.db import models

class Admin (models.Model):
    uid = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class FundingRequest (models.Model):
    uid = models.IntegerField()
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    requestType = models.CharField(max_length=20)
    requestCategory = models.CharField(max_length=20)
    grantCategory = models.CharField(max_length=20)
    eventType = models.CharField(max_length=20)
    fundingRound = models.CharField(max_length=20)
    studentGroup = models.CharField(max_length=40)
    requestStatus = models.CharField(max_length=20)
    
class GraduateRequest(FundingRequest):
    academicDepartmentalAffiliate = models.CharField(max_length=20)
    gaDelegate = models.CharField(max_length=20)
    studentOrgMemTot = models.IntegerField()
    studentOrgGrad = models.IntegerField()
    studentOrgUnd = models.IntegerField()
    attendedWaiver = models.BooleanField()
    
class UndergraduateRequest(FundingRequest):
    studentOrgTot = models.IntegerField()
    stduentOrgStud = models.IntegerField()
    attended = models.BooleanField()
    
class TravelRequest(FundingRequest):
    requestingAs = models.CharField(max_length=20)

class Budget(models.Model):
    additionalInfo = models.CharField(max_length=2000)
    amountAwarded = models.DecimalField(max_digits=10,decimal_places=2)
    comment = models.CharField(max_length=200)
    totalRequestedAmount = models.DecimalField(max_digits=10,decimal_places=2)
    totalOtherFunding = models.DecimalField(max_digits=10,decimal_places=2)
    requestedTotal = models.DecimalField(max_digits=10,decimal_places=2)

class ItemDescription(models.Model):
    budget = models.ForeignKey(Budget)
    description = models.CharField(max_length=30)
    comment = models.CharField(max_length=100)
    quantity = models.IntegerField()
    itemCost = models.DecimalField(max_digits=10,decimal_places=2)
    requestedAmount = models.DecimalField(max_digits=10,decimal_places=2)
    otherFunding = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)

class Event(models.Model):
    fundingRequest = models.ForeignKey(FundingRequest)
    eventTitle = models.CharField(max_length=30)
    description = models.CharField(max_length=2000)
    sameBudgetForRecurringEvents = models.BooleanField()
    startDate = models.DateField('%m/%d/%y')
    endDate = models.DateField('%m/%d/%y')
    location = models.CharField(max_length=30)
    waiverRequested = models.BooleanField()
    attendenceNonStudent = models.IntegerField()
    attendenceUnd = models.IntegerField()
    attendenceGrad = models.IntegerField()
    budget = models.ForeignKey(Budget)
    
class TravelEvent(Event):
    depatureDate = models.DateField('%m/%d/%y')
    returnDate = models.DateField('%m/%d/%y')
    presenting = models.BooleanField()
    presentationTitle = models.CharField(max_length=30)
    
class Config(models.Model):
    pass
    
class ConfigAdmin (models.Model):
    config = models.ForeignKey(Config)
    email = models.CharField(max_length=30)
    
class ConfigLocation (models.Model):
    config = models.ForeignKey(Config)
    location = models.CharField(max_length=30)

class ConfigUGReqCat (models.Model):
    config = models.ForeignKey(Config)
    category = models.CharField(max_length=30)
    
class ConfigGradReqCat (models.Model):
    config = models.ForeignKey(Config)
    category = models.CharField(max_length=30) 

class ConfigUGGrant (models.Model):
    config = models.ForeignKey(Config)
    category = models.CharField(max_length=30) 
    
class ConfigGradGrant (models.Model):
    config = models.ForeignKey(Config)
    category = models.CharField(max_length=30) 

class ConfigFundingRound (models.Model):
    config = models.ForeignKey(Config)
    name = models.CharField(max_length=30)
    deadline = models.DateField('%m/%d/%Y')

class ConfigGradDelegate (models.Model):
    config = models.ForeignKey(Config)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    