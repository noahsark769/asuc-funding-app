from django.db import models

class Admin (models.Model):
    UId = models.CharField(max_length=30)
    email = models.Charfield(max_length=30)

class FundingRequest (models.Model):
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    requestCategory = models.CharField(max_length=20)
    grantCategory = odels.CharField(max_length=20)
    eventType = models.CharField(max_length=20)
    fundingRound = models.CharField(max_length=20)
    sponsoringStudentGroup = models.CharField(max_length=40)
    
class GraduateRequest(FundingRequest):
    academicDepartmentalAffilliate = models.CharField(max_length=20)
    gaDelegate = models.CharField(max_length=20)
    studentOrgMemTot = models.IntegerField(min_value=0, max_value=99999)
    studentOrgGrad = models.IntegerField(min_value=0, max_value=99999)
    studentOrgUnd = models.IntegerField(min_value=0, max_value=99999)
    AttendedWaiver = models.BooleanField()
    
class Undergraduate(FundingRequest):
    studentOrgTot = models.IntegerField(min_value=0, max_value=99999)
    stduentOrgStud = models.IntegerField(min_value=0, max_value=99999)
    attened = models.BooleanField()
    
class Travel(FundingRequest):
    requestingAs = models.CharField(max_length=20)
    
    
class Event(models.Model):
    eventTitle = models.CharField(max_length=30)
    description = models.CharField(max_length=2000)
    sameBudgetForRecurringEvents = models.BooleanField()
    startDate = models.DateField('%m/%d/%y')
    endDate = models.DateField('%m/%d/%y')
    location = models.CharField(max_length=30)
    waiverRequested = models.BooleanField()
    attendenceNonStudent = models.IntegerField(min_value=0, max_value=99999)
    attendenceUnd = models.IntegerField(min_value=0, max_value=99999)
    attendenceGrad = models.IntegerField(min_value=0, max_value=99999)
    budgetDetail = manyToManyField(BudgetDetail)
    
class TravelEvent(Event):
    depatureDate = models.DateField('%m/%d/%y')
    returnDate = models.DateField('%m/%d/%y')
    presenting = models.BooleanField
    presentationTitle = models.CharField(max_length=30)

class BudgetDetail(models.Model):
    itemDescription = manytoManyField(ItemDescription)
    additionalInfo = models.CharField(max_length=2000)
    ammountAwarded = models.DecimalField(max_digits=10,decimal_places=2)
    comment = models.CharField(max_length=200)

class ItemDescription(models.Model):
    description = models.CharField(max_length=30)
    comment = models.CharField(max_length=100)
    quantity = models.IntegerField(min_value=0, max_value=9999)
    itemCost = models.DecimalField(max_digits=10,decimal_places=2)
    requestedAmount = models.DecimalField(max_digits=10,decimal_places=2)
    otherFunding = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)
    
class Config(models.Model):
    
class ConfigAdmin (models.Model):
    config = models.ForeignKey(Config)
    email = models.Charfield(max_length=30)
    
class ConfigEvents (models.Model):
    config = models.ForeignKey(Config)
    eventLocation = models.Charfield(max_length=30)

class ConfigUGReqCat (models.Model):
    config = models.ForeignKey(Config)
    category = models.Charfield(max_length=30)
    
class ConfigGRReqCat (models.Model):
    config = models.ForeignKey(Config)
    category = models.Charfield(max_length=30) 

class ConfigUGGrant (models.Model):
    config = models.ForeignKey(Config)
    category = models.Charfield(max_length=30) 
    
class configGradGrant (models.Model):
    config = models.ForeignKey(Config)
    category = models.Charfield(max_length=30) 

class FundinRounds (models.Model):
    config = models.ForeignKey(Config)
    name = models.Charfield(max_length=30)
    deadline = models.DateField('%m/%d/%Y')

class GradDelegates (models.Model):
    config = models.ForeignKey(Config)
    name = models.Charfield(max_length=30)
    email = models.Charfield(max_length=30)

    