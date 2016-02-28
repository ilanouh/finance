from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import TemplateView
from django.core import serializers
from .models import Client, Account


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
		accounts = Account.objects.all().filter(client_id=client)
		# print accounts
		# for a in accounts:
			# print a.client_id


		return context


class PersonalView(TemplateView):
	template_name = 'bar/personal.html'

	def get_context_data(self, **kwargs):
		context = super(PersonalView, self).get_context_data(**kwargs)
		client = Client.objects.get(client_id=kwargs['slug'])
		# context['money'] = get_object_or_404(Account, account_id='CL42Co3')
		json_serializer = serializers.get_serializer("json")()
		context['accounts'] = json_serializer.serialize(Account.objects.all().filter(client_id=client), ensure_ascii=False)
		# accounts = Account.objects.all().filter(client_id=client)
		# print accounts
		# for a in accounts:
			# print a.client_id
		return context
