from __future__ import unicode_literals
# from django.utils.translation import ugettext_lazy as _

from django.db import models

# Create your models here.


class	Client(models.Model):
	GENDER_CHOICES = (
		('H', 'male'),
		('F', 'female'),
	)
	STATUS_CHOICES = (
		('Actif', 'active'),
		('Inactif', 'inactive'),
		('Retraite', 'retired'),
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
	risk_profile = models.CharField('risk profile', null=True, blank=True, max_length=100)
	enter_date = models.DateTimeField('enter date', null=True, blank=True)

