from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import TemplateView

from .models import Account


class IndexView(TemplateView):
	template_name = 'bar/index.html'


class GraphView(TemplateView):
	template_name = 'foo/graph.html'

	def get_context_data(self, **kwargs):
		context = super(GraphView, self).get_context_data(**kwargs)
		context['money'] = get_object_or_404(Account, account_id='CL42Co3')

		return context
