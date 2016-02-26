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
		('Compte titres', 'Securities Account'),
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


# class		AccountTrackRecordEvolution(object):


		
