from django.db import models

class Admin (models.Model):
	uid = models.IntegerField()
	email = models.CharField(max_length=50)

class Budget(models.Model):
	additionalInfo = models.CharField(max_length=5000)
	amountAwarded = models.DecimalField(max_digits=10,decimal_places=2)
	comment = models.CharField(max_length=500)
	totalRequestedAmount = models.DecimalField(max_digits=10,decimal_places=2)
	totalOtherFunding = models.DecimalField(max_digits=10,decimal_places=2)
	grandTotal = models.DecimalField(max_digits=10,decimal_places=2)

	def items(self):
		return self.itemdescription_set.all()

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
	contingency = models.BooleanField()
	studentGroup = models.CharField(max_length=50)
	studentGroupPending = models.BooleanField()
	requestStatus = models.CharField(max_length=50)
	dateSubmitted = models.DateField(auto_now=True)
	eventTitle = models.CharField(max_length=50)
	description = models.CharField(max_length=5000)
	sameBudgetForRecurringEvents = models.BooleanField()
	budget = models.OneToOneField(Budget, null=True)

	def compute_requested_total(self):
		if self.eventType == 'Operational Costs':
			return self.budget.totalRequestedAmount
		requestedTotal = 0
		for event in self.event_set.all():
			requestedTotal += event.budget.totalRequestedAmount
		return requestedTotal

	def compute_awarded_total(self):
		if self.eventType == 'Operational Costs':
			return self.budget.amountAwarded
		awardedTotal = 0
		for event in self.event_set.all():
			awardedTotal += event.budget.amountAwarded
		return awardedTotal

	def date_submitted_formatted(self):
		return str(self.dateSubmitted.month) + '/' + str(self.dateSubmitted.day) + '/' + str(self.dateSubmitted.year)

	def grant_categories(self):
		return 'Grant' in self.requestCategory.split(',')

	def split_grant_category(self):
		return self.grantCategory.split(',')

	def split_req_category(self):
		return self.requestCategory.split(',')

	def events(self):
		return self.event_set.all()

	def single_event(self):
		return self.event_set.all()[0]

	def budget_items(self):
		return self.event_set.all()[0].budget.itemdescription_set.all()

	def own_budget_items(self):
		return self.budget.itemdescription_set.all()

	def formattedID(self):
		return '%06d' % self.id;
	
class GraduateRequest(FundingRequest):
	academicDepartmentalAffiliate = models.CharField(max_length=50)
	gaDelegate = models.CharField(max_length=100)
	studentOrgTot = models.IntegerField()
	studentOrgGrad = models.IntegerField()
	studentOrgUG = models.IntegerField()
	attendedWaiver = models.BooleanField()
	
class UndergraduateRequest(FundingRequest):
	studentOrgTot = models.IntegerField()
	studentOrgStud = models.IntegerField()
	attended = models.BooleanField()
	
class TravelRequest(FundingRequest):
	requestingAs = models.CharField(max_length=50)

class ItemDescription(models.Model):
	budget = models.ForeignKey(Budget)
	description = models.CharField(max_length=100)
	comment = models.CharField(max_length=500)
	quantity = models.IntegerField()
	itemCost = models.DecimalField(max_digits=10,decimal_places=2)
	requestedAmount = models.DecimalField(max_digits=10,decimal_places=2)
	otherFunding = models.DecimalField(max_digits=10,decimal_places=2)
	total = models.DecimalField(max_digits=10,decimal_places=2)

	def itemCostF(self):
		return "%0.2f" % self.itemCost
	def requestedAmountF(self):
		return "%0.2f" % self.requestedAmount
	def otherFundingF(self):
		return "%0.2f" % self.otherFunding
	def totalF(self):
		return "%0.2f" % self.total

class Event(models.Model):
	fundingRequest = models.ForeignKey(FundingRequest)
	startDate = models.DateField('%m/%d/%y')
	endDate = models.DateField('%m/%d/%y')
	location = models.CharField(max_length=100)
	waiverRequested = models.CharField(max_length=10)
	attendenceNonStudent = models.IntegerField()
	attendenceUG = models.IntegerField()
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