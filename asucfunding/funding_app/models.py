from django.db import models

class Admin (models.Model):
    uid = models.IntegerField()
    email = models.CharField(max_length=50)

class FundingRequest (models.Model):
    uid = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    requestType = models.CharField(max_length=50)
    requestCategory = models.CharField(max_length=50)
    grantCategory = models.CharField(max_length=50)
    eventType = models.CharField(max_length=50)
    fundingRound = models.CharField(max_length=50)
    studentGroup = models.CharField(max_length=50)
    requestStatus = models.CharField(max_length=50)
    dateSubmitted = models.DateTimeField(auto_now=True)

    def compute_requested_total(self):
        requestedTotal = 0
        for event in self.event_set.all():
            requestedTotal += event.budget.requestedTotal
        return requestedTotal

    def compute_awarded_total(self):
        awardedTotal = 0
        for event in self.event_set.all():
            awardedTotal += event.budget.awardedTotal
        return awardedTotal
    
class GraduateRequest(FundingRequest):
    academicDepartmentalAffiliate = models.CharField(max_length=50)
    gaDelegate = models.CharField(max_length=50)
    studentOrgMemTot = models.IntegerField()
    studentOrgGrad = models.IntegerField()
    studentOrgUnd = models.IntegerField()
    attendedWaiver = models.BooleanField()
    
class UndergraduateRequest(FundingRequest):
    studentOrgTot = models.IntegerField()
    stduentOrgStud = models.IntegerField()
    attended = models.BooleanField()
    
class TravelRequest(FundingRequest):
    requestingAs = models.CharField(max_length=50)

class Budget(models.Model):
    additionalInfo = models.CharField(max_length=5000)
    amountAwarded = models.DecimalField(max_digits=10,decimal_places=2)
    comment = models.CharField(max_length=500)
    totalRequestedAmount = models.DecimalField(max_digits=10,decimal_places=2)
    totalOtherFunding = models.DecimalField(max_digits=10,decimal_places=2)
    requestedTotal = models.DecimalField(max_digits=10,decimal_places=2)

class ItemDescription(models.Model):
    budget = models.ForeignKey(Budget)
    description = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    quantity = models.IntegerField()
    itemCost = models.DecimalField(max_digits=10,decimal_places=2)
    requestedAmount = models.DecimalField(max_digits=10,decimal_places=2)
    otherFunding = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)

class Event(models.Model):
    fundingRequest = models.ForeignKey(FundingRequest)
    eventTitle = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    sameBudgetForRecurringEvents = models.BooleanField()
    startDate = models.DateField('%m/%d/%y')
    endDate = models.DateField('%m/%d/%y')
    location = models.CharField(max_length=100)
    waiverRequested = models.BooleanField()
    attendenceNonStudent = models.IntegerField()
    attendenceUnd = models.IntegerField()
    attendenceGrad = models.IntegerField()
    budget = models.ForeignKey(Budget)
    
class TravelEvent(Event):
    depatureDate = models.DateField('%m/%d/%y')
    returnDate = models.DateField('%m/%d/%y')
    presenting = models.BooleanField()
    presentationTitle = models.CharField(max_length=50)
    
class ConfigAdmin (models.Model):
    email = models.CharField(max_length=50)
    
class ConfigLocation (models.Model):
    location = models.CharField(max_length=50)

class ConfigUGReqCat (models.Model):
    category = models.CharField(max_length=50)
    
class ConfigGradReqCat (models.Model):
    category = models.CharField(max_length=50) 

class ConfigUGGrant (models.Model):
    category = models.CharField(max_length=50) 
    
class ConfigGradGrant (models.Model):
    category = models.CharField(max_length=50) 

class ConfigFundingRound (models.Model):
    name = models.CharField(max_length=50)
    deadline = models.DateField('%m/%d/%Y')

class ConfigGradDelegate (models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    