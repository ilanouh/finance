import csv

from django.db import models
from bar.models import Account, AccountAnalytic

def fill_clients(request, file):
	field = ['client_id', 'period', 'date_start', 'date_end', 'account_p', 'account_perf', 'account_vol', 'account_maxdd', 'account_te', 'bench_p', 'bench_perf', 'bench_perfann', 'bench_vol', 'bench_maxdd']
	f = open(file)
	for row in csv.reader(f):
		datas = row[0].split(';')
		datas[0] = Account.objects.get(account_id=datas[0])
		
		AccountAnalytic.objects.create(**dict(zip(field, row)))
	return field


def fill_accounts(request, file):
	field = ['account_id', 'period', 'date_start', 'date_end', 'account_p', 'account_perf', 'account_vol', 'account_maxdd', 'account_te', 'bench_p', 'bench_perf', 'bench_perfann', 'bench_vol', 'bench_maxdd']
	f = open(file)
	for row in csv.reader(f):
		datas = row[0].split(';')
		datas[0] = Account.objects.get(account_id=datas[0])
		
		AccountAnalytic.objects.create(**dict(zip(field, row)))
	return field


def fill_account_analytics(request, file):
	field = ['account_id', 'period', 'date_start', 'date_end', 'account_p', 'account_perf', 'account_vol', 'account_maxdd', 'account_te', 'bench_p', 'bench_perf', 'bench_perfann', 'bench_vol', 'bench_maxdd']
	f = open(file)
	for row in csv.reader(f):
		datas = row[0].split(';')
		datas[0] = Account.objects.get(account_id=datas[0])
		
		AccountAnalytic.objects.create(**dict(zip(field, row)))
	return field
