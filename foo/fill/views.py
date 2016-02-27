import csv

from django.shortcuts import redirect
from datetime import datetime
from django.db import models
from bar.models import Client, Account, AccountAnalytic
from django.core.exceptions import ObjectDoesNotExist


def fill_clients(request, file):
	field = ['client_id', 'first_name', 'last_name', 'gender', 'birth_date', 'status', 'job', 'society', 'children', 'region', 'risk_profile', 'enter_date']
	f = open(file)
	for row in csv.reader(f):
		datas = row[0].split(';')
		if datas[8].replace(" ","") == "-":
			datas[8] = 0
		datas[4] = datetime.strptime(datas[4], '%d/%m/%Y')
		datas[11] = datetime.strptime(datas[11], '%d/%m/%Y')
		try:
 			Client.objects.get(client_id=datas[0])
		except ObjectDoesNotExist:
			Client.objects.create(
				client_id=datas[0].decode('unicode-escape'),
				first_name=datas[1].decode('unicode-escape'),
				last_name=datas[2].decode('unicode-escape'),
				gender=datas[3].decode('unicode-escape'),
				birth_date=datas[4],
				status=datas[5].decode('unicode-escape'),
				job=datas[6].decode('unicode-escape'),
				society=datas[7].decode('unicode-escape'),
				children=datas[8],
				region=datas[9].decode('unicode-escape'),
				risk_profile=datas[10].decode('unicode-escape'),
				enter_date=datas[11],
			)
	return redirect('index')


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
