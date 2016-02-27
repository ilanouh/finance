import csv

from django.db import models
# from __future__ import unicode_literals

class		AccountAnalytics(object):

		account_id = models.CharField(max_lenght=250, unique=True)
		period = models.CharField(max_lenght=250)
		date_start = models.CharField(max_lenght=250)
		date_end = models.CharField(max_lenght=250)
		account_p = models.CharField(max_lenght=250)
		account_perf = models.CharField(max_lenght=250)
		account_vol = models.CharField(max_lenght=250)
		accound_maxdd = models.CharField(max_lenght=250)
		account_te = models.CharField(max_lenght=250)
		bench_p = models.CharField(max_lenght=250)
		bench_perf = models.CharField(max_lenght=250)
		bench_perfann = models.CharField(max_lenght=250)
		bench_vol = models.CharField(max_lenght=250)
		bench_maxdd = models.CharField(max_lenght=250)

def parse_csv(file):
	field = ['account_id', 'period', 'date_start', 'date_end', 'account_p', 'account_perf', 'account_vol', 'account_maxdd', 'account_te', 'bench_p', 'bench_perf', 'bench_perfann', 'bench_vol', 'bench_maxdd']
	f = open(file)
	# with open(file) as f
	for row in csv.reader(f):
		AccountAnalytics.objects.create(**dict(zip(fields, row)))
	return field

def	print_stuff(to_print):
	print to_print

		
# file = input("What file do you want to parse ?")
# print(parse_csv(file, field))
