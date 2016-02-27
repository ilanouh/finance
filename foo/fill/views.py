import csv

from datetime import datetime
from django.db import models
from bar.models import Client, Account, AccountAnalytic
from django.core.exceptions import ObjectDoesNotExist

# from django.utils import formats

def fill_clients(request, file):
	field = ['client_id', 'first_name', 'last_name', 'gender', 'birth_date', 'status', 'job', 'society', 'children', 'region', 'risk_profile', 'enter_date']
	f = open(file)
	for row in csv.reader(f):
		datas = row[0].split(';')
		# datas[0] = Account.objects.get(account_id=datas[0])
		# date_list = datas[4].split('/')
		# date_str = date_list[0] + date_list[1] + date_list[2]
		if datas[8].replace(" ","") == "-":
			datas[8] = 0
		datas[4] = datetime.strptime(datas[4], '%d/%m/%Y')
		datas[11] = datetime.strptime(datas[11], '%d/%m/%Y')
		print datas
		print type(datas[5])
		# print unicode(datas[5], 'utf-8')
		try:
 			Client.objects.get(client_id=datas[0])
		except ObjectDoesNotExist:
			print "CREATE"
			Client.objects.create(
				client_id=unicode(datas[0], 'utf-8'),
				first_name=unicode(datas[1], 'utf-8'),
				last_name=unicode(datas[2], 'utf-8'),
				gender=unicode(datas[3], 'utf-8'),
				birth_date=datas[4],
				status=unicode(datas[5], 'utf-8'),
				job=unicode(datas[6], 'utf-8'),
				society=unicode(datas[7], 'utf-8'),
				children=datas[8],
				region=unicode(datas[9], 'utf-8'),
				risk_profile=unicode(datas[10], 'utf-8'),
				enter_date=datas[11],
			)
		# Client.objects.create(**dict(zip(field, datas)))
	return field


def fill_accounts(request, file):
	field = ['account_id', 'period', 'date_start', 'date_end', 'account_p', 'account_perf', 'account_vol', 'account_maxdd', 'account_te', 'bench_p', 'bench_perf', 'bench_perfann', 'bench_vol', 'bench_maxdd']
	f = open(file)
	for row in csv.reader(f):
		datas = row[0].split(';')
		datas[0] = Account.objects.get(account_id=datas[0])
		
		Account.objects.create(**dict(zip(field, datas)))
	return field


def fill_account_analytics(request, file):
	field = ['account_id', 'period', 'date_start', 'date_end', 'account_p', 'account_perf', 'account_vol', 'account_maxdd', 'account_te', 'bench_p', 'bench_perf', 'bench_perfann', 'bench_vol', 'bench_maxdd']
	f = open(file)
	for row in csv.reader(f):
		datas = row[0].split(';')
		datas[0] = Account.objects.get(account_id=datas[0])
		
		AccountAnalytic.objects.create(**dict(zip(field, datas)))
	return field
