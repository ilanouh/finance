from __future__ import unicode_literals
# from django.utils.translation import ugettext_lazy as _

from django.db import models

# Create your models here.


class	Client(models.Model):
	GENDER_CHOICES = (
		('H', 'Male'),
		('F', 'Female'),
	)
	STATUS_CHOICES = (
		('Actif', 'Active'),
		('Inactif', 'Inactive'),
		('Retraite', 'Retired')
	)
	RISK_CHOICES = (
		('Dynamique', 'Dynamic'),
		('Defensif', 'Defensive'),
		('Equilibre', 'Balanced')
	)

	client_id = models.CharField('client id', max_length=250, unique=True)
	first_name = models.CharField('first name', max_length=250)
	last_name = models.CharField('last name', max_length=250)
	gender = models.CharField('gender', choices=GENDER_CHOICES, default="H", max_length=5)
	birth_date = models.DateTimeField('birth date')
	status = models.CharField('activity status', choices=STATUS_CHOICES, default="Actif", max_length=25)
	job = models.CharField('job', max_length=100)
	society = models.CharField('society', max_length=100)
	children = models.IntegerField('children', default=0)
	region = models.CharField('region', max_length=100)
	risk_profile = models.CharField('risk profile', choices=RISK_CHOICES, null=True, blank=True, max_length=100)
	enter_date = models.DateTimeField('enter date', null=True, blank=True)

	def __str__(self):
		return self.client_id


class		Account(models.Model):
	TYPE_CHOICES = (
		('Assurance vie', 'Life Insurance'),
		('Compte titres', 'Trading Account'),
		('PEA', 'Equity Savings Plan')
	)
	PROFILE_CHOICES = (
		('Dynamique', 'Dynamic'),
		('Defensif', 'Defensive'),
		('Equilibre', 'Balanced')
	)
	account_id = models.CharField('account id', max_length=250, unique=True)
	client_id = models.ForeignKey(Client)
	initial_date = models.DateTimeField('initial date')
	initial_amount = models.FloatField('initial amount')
	final_amount = models.FloatField('final amount')
	account_type = models.CharField('account type', choices=TYPE_CHOICES, max_length=100)
	profile = models.CharField('profile', max_length=100)

	def __str__(self):
		return self.account_id


class AccountAnalytic(models.Model):
	account_id = models.ForeignKey(Account)
	period = models.IntegerField('period')
	date_start = models.DateTimeField('Date start')
	date_end = models.DateTimeField('Date end')
	account_pl = models.FloatField('Account profit & loss')
	account_perf = models.FloatField('Account Performance')
	account_perf_ann = models.FloatField('Account Performance annualisee')
	account_vol = models.FloatField('Account Volatilite')
	account_max_dd = models.FloatField('Account Maximum Drawdown')
	account_te = models.FloatField('Account Tracking-error')
	bench_pl = models.FloatField('Bench profit & loss')
	bench_perf = models.FloatField('Bench performance')
	bench_perf_ann = models.FloatField('Bench performance annualisee')
	bench_vol = models.FloatField('Bench Volatilite')
	bench_max_dd = models.FloatField('Bench Maximum Drawdown')

	def __str__(self):
		return self.account_id


class Product(models.Model):
	# CURRENCY_CHOICES = (
		# ('EUR', 'Euros'),
		# ('USD', 'US Dollars')
	# )
	isin = models.CharField('ISIN', unique=True, max_length=250)
	name = models.CharField('name', max_length=250)
	product_type = models.CharField('type', max_length=250)
	pea = models.BooleanField('equity savings plan', default=False)
	asv = models.BooleanField('life insurance', default=False)
	cto = models.BooleanField('trading account', default=False)
	asset = models.CharField('asset', max_length=250)
	zone = models.CharField('zone', max_length=250)
	focus = models.CharField('focus', max_length=250)
	currency = models.CharField('currency', max_length=50)
	# currency = models.CharField('currency', max_length=50, choices=CURRENCY_CHOICES)
	management = models.CharField('management', max_length=100)
	description = models.TextField('description', max_length=1000)


# class		AccountTrackRecordEvolution(object):


		
