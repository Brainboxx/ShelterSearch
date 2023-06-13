from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Agents
from properties.models import Property

# Create your views here.
class AgentListView(ListView):
    model = Agents
    template_name = 'agents/agents-grid.html'
    paginate_by = 6

    def get_queryset(self):
        return super().get_queryset().all()

class AgentDetailView(DetailView):
    model = Agents
    template_name = 'agents/agent-detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        agent = self.get_object()

        properties = agent.property_set.all()
        num_of_agent_properties = len(properties)

        context['num_of_agent_properties'] = num_of_agent_properties
        context['properties'] = properties
        return context
