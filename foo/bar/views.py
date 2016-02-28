from django.shortcuts import render, render_to_response, get_object_or_404, _get_queryset
from django.views.generic import TemplateView, DetailView
from django.core import serializers
from .models import Client, Account

def get_object_or_none(klass, *args, **kwargs):
    queryset = _get_queryset(klass)
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        return None

class IndexView(TemplateView):
	template_name = 'bar/index.html'


class GraphView(TemplateView):
	template_name = 'foo/graph.html'

	def get_context_data(self, **kwargs):
		context = super(GraphView, self).get_context_data(**kwargs)
		client = Client.objects.get(client_id=36)
		# context['money'] = get_object_or_404(Account, account_id='CL42Co3')
		json_serializer = serializers.get_serializer("json")()
		context['accounts'] = json_serializer.serialize(Account.objects.all().filter(client_id=client), ensure_ascii=False)
		# accounts = Account.objects.all().filter(client_id=client)
		# print accounts
		# for a in accounts:
			# print a.client_id


		return context


class ClientView(TemplateView):
	template_name = 'bar/personal.html'

	def get_context_data(self, **kwargs):
		context = super(ClientView, self).get_context_data(**kwargs)
		# context['client'] = get_object_or_404(Client, client_id=kwargs['client_id'])
		context['object'] = get_object_or_404(Client, client_id=kwargs['client_id'])
		# context['accounts'] = get_object_or_none(Client, client_id=kwargs['client_id'])
		context['accounts'] = Account.objects.filter(client_id=context['object'])
	# 	# context['account'] = get_object_or_404(Account, account_id=client)
	# 	# json_serializer = serializers.get_serializer("json")()
	# 	# context['accounts'] = json_serializer.serialize(Account.objects.all().filter(client_id=client), ensure_ascii=False)
	# 	# accounts = Account.objects.all().filter(client_id=client)
	# 	# print accounts
	# 	# for a in accounts:
	# 		# print a.client_id
		return context


class AccountView(TemplateView):
	template_name = 'bar/account.html'

	def get_context_data(self, **kwargs):
		context = super(AccountView, self).get_context_data(**kwargs)
		# context['client'] = get_object_or_404(Client, client_id=kwargs['client_id'])
		context['object'] = get_object_or_404(Account, account_id=kwargs['account_id'])
	# 	# context['account'] = get_object_or_404(Account, account_id=client)
	# 	# json_serializer = serializers.get_serializer("json")()
	# 	# context['accounts'] = json_serializer.serialize(Account.objects.all().filter(client_id=client), ensure_ascii=False)
	# 	# accounts = Account.objects.all().filter(client_id=client)
	# 	# print accounts
	# 	# for a in accounts:
	# 		# print a.client_id
		return context


class SimulationView(TemplateView):
	template_name = 'bar/simulation.html'
