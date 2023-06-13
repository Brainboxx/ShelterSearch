from django.urls import path
from .views import AgentListView, AgentDetailView

urlpatterns = [
    path('', AgentListView.as_view(), name='agents-list'),
    path('agent/<int:pk>', AgentDetailView.as_view(), name='agent-detail')
]