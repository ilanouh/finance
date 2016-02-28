import csv

from django.template.defaultfilters import slugify
from django.shortcuts import redirect
from datetime import datetime
from django.db import models
from bar.models import Client, Account, AccountAnalytic, Product, ProductAnalytic, ProductTrackRecordEvolution, AccountTrackRecordComposition, AccountTrackRecordEvolution
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
				last_name=datas[1].decode('unicode-escape'),
				first_name=datas[2].decode('unicode-escape'),
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
	field = ['account_id', 'client_id', 'initial_date', 'initial_amount', 'final_amount', 'account_type', 'profile']
	f = open(file)
	for row in csv.reader(f):
		datas = row[0].split(';')
		datas[2] = datetime.strptime(datas[2], '%d/%m/%Y')
		try:
			client = Client.objects.get(client_id=datas[1])
			try:
			 	Account.objects.get(account_id=datas[0])
			except ObjectDoesNotExist:
				Account.objects.create(
					account_id=datas[0].decode('unicode-escape'),
					client_id=client,
					initial_date=datas[2],
					initial_amount=datas[3],
					final_amount=datas[4],
					account_type=datas[5].decode('unicode-escape'),
					profile=datas[6].decode('unicode-escape'),
				)
		except ObjectDoesNotExist:
			print "CLIENT DOESN'T EXIST"
	return redirect('index')


def fill_products(request, file):

	field = ['isin', 'name', 'product_type', 'pea', 'asv', 'cto', 'asset', 'zone', 'focus', 'currency', 'management', 'description']
	f = open(file)
	for row in csv.reader(f):
		datas = row[0].split(';')
		try:
			Product.objects.get(isin=datas[0])
		except ObjectDoesNotExist:
			Product.objects.create(
				isin = datas[0].decode('unicode-escape'),
				name = datas[1].decode('unicode-escape'),
				product_type = datas[2].decode('unicode-escape'),
				pea = True if datas[3] == "Yes" else False,
				asv = True if datas[4] == "Yes" else False,
				cto = True if datas[5] == "Yes" else False,
				asset = datas[6].decode('unicode-escape'),
				zone = datas[7].decode('unicode-escape'),
				focus = datas[8].decode('unicode-escape'),
				currency = datas[9].decode('unicode-escape'),
				management = datas[10].decode('unicode-escape'),
				description = datas[11].decode('unicode-escape'),
			)
	return redirect('index')


def fill_product_analytics(request, file):
	field = ['isin', 'period', 'date_start', 'date_end', 'pl', 'perf', 'perf_ann', 'vol', 'max_dd']
	f = open(file)
	for row in csv.reader(f):
		data = row[0].split(';')
		data[2] = datetime.strptime(data[2], '%d/%m/%Y')
		data[3] = datetime.strptime(data[3], '%d/%m/%Y')
		try:
			isin = Product.objects.get(isin=data[0])
			try:
				ProductAnalytic.objects.get(isin=isin)
			except ObjectDoesNotExist:
				ProductAnalytic.objects.create(
					isin = isin,
					period = data[1].decode('unicode-escape'),
					date_start = data[2],
					date_end = data[3],
					pl = data[4],
					perf = data[5],
					perf_ann = data[6],
					vol = data[7],
					max_dd = data[8],
				)
		except ObjectDoesNotExist:
			print "PRODUCT DOES NOT EXIST!"
	return redirect('index')


def fill_account_analytics(request, file):
	field = ['account_id', 'period', 'date_start', 'date_end', 'account_pl', 'account_perf', 'account_perf', 'account_vol', 'account_max_dd', 'account_te', 'bench_pl', 'bench_perf', 'bench_perf_ann', 'bench_vol', 'bench_max_dd']
	f = open(file)
	for row in csv.reader(f):
		data = row[0].split(';')
		data[2] = datetime.strptime(data[2], '%d/%m/%Y')
		data[3] = datetime.strptime(data[3], '%d/%m/%Y')
		try:
			account_id = Account.objects.get(account_id=data[0])
		except ObjectDoesNotExist:
			AccountAnalytic.objects.create(
				account_id = data[0].decode('unicode-escape'),
				period = data[1],
				date_start = data[2],
				date_end = data[3],
				account_pl = data[4],
				account_perf = data[5],
				account_vol = data[6],
				account_max_dd = data[7],
				account_te = data[8],
				bench_pl = data[9],
				bench_perf = data[10],
				bench_perf_ann = data[11],
				bench_vol = data[12],
				bench_max_dd = data[13],
				)
	return redirect('index')

def fill_product_track_record_evolution(request, file):
	field = ['isin','date','value']
	f = open(file)
	for row in csv.reader(f):
		data = row[0].split(';')
		data[1] = datetime.strptime(data[1], '%d/%m/%Y')
		try:
			isin = Product.objects.get(isin=data[0])
			try:
				ProductTrackRecordEvolution.objects.get(date=data[1])
			except ObjectDoesNotExist:
				ProductTrackRecordEvolution.objects.create(
					isin = isin,
					date = data[1],
					value = data[2],
					)
		except ObjectDoesNotExist:
			print "PRODUCT DOES NOT EXIST!"
	return redirect('index')

def fill_account_track_record_composition(request, file):
	field = ['account_id', 'date', 'isin', 'amount', 'client_decided']
	f = open(file)
	for row in csv.reader(f):
		data = row[0].split(';')
		data[1] = datetime.strptime(data[1], '%d/%m/%Y')
		try:
			account_id = Account.objects.get(account_id=data[0])
		except ObjectDoesNotExist:
			AccountTrackRecordComposition.objects.create(
				account_id = data[0].decode('unicode-escape'),
				date = data[1],
				isin = data[2],
				amount = data[3],
				client_decided = data[4],
				)
	return redirect('index')


def fill_account_track_record_evolution(request, file):
	field = [ 'account_id', 'date', 'account_amount', 'bench_amount', 'account_perf_daily', 'bench_perf_daily', 'diff_perf_daily']
	f = open(file)
	for row in csv.reader(f):
		data = row[0].split(';')
		data[1] = datetime.strptime(data[1], '%d/%m/%Y')
		try:
			account_id = Account.objects.get(account_id=data[0])
			try:
				AccountTrackRecordEvolution.objects.get(date=data[1])
			except ObjectDoesNotExist:
				AccountTrackRecordEvolution.objects.create(
					account_id = data[0].decode('unicode-escape'),
					date = data[1],
					account_amount = data[2],
					bench_amount = data[3],
					account_perf_daily = data[4],
					bench_perf_daily = data[5],
					diff_perf_daily = data[6],
					)
		except ObjectDoesNotExist:
			print "ACCOUNT DOESNT EXIST"
	return redirect('index')




