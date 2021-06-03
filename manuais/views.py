from django.shortcuts import render, reverse
from django.urls import reverse_lazy 
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.edit import UpdateView 
from manuais.models import Equipamentos, RevisaoManuais 
from manuais.forms import EquipamentosForm, RevisaomanualForm   

# --- equipamentos views --- #
class EquipamentosIndexView(TemplateView):
	template_name = 'equipamento/index-equipamentos.html'

class EquipamentosNewView(CreateView):
	template_name = 'equipamento/equipamento-novo.html'
	form_class = EquipamentosForm
	success_url = reverse_lazy('equipamentos')
	success_message = 'Equipamento Cadastrado com sucesso'

class EquipamentosDeleteView(DeleteView):
	model = Equipamentos
	template_name = 'equipamento/equipamento-delete.html'
	success_url = reverse_lazy('equipamentos')
	success_message = 'O equipamento foi deletado com sucesso'

class EquipamentosUpdateView(UpdateView):
	model = Equipamentos
	form_class = EquipamentosForm
	template_name = 'equipamento/equipamento-alterar.html'
	success_url = reverse_lazy('equipamentos')
	success_message = 'As alterações foram efectuadas com sucesso'

class EquipamentosListView(ListView):
	model = Equipamentos
	template_name = 'equipamento/equipamentos.html'


# --- manuais views --- #
class ManuaisIndexView(TemplateView):
	template_name = 'manuais/index-manuais.html'

class ManuaisNewView(CreateView):
	template_name = 'manuais/manual-novo.html'
	form_class = RevisaomanualForm
	success_url = reverse_lazy('equipamentos')
	success_message = 'Manual Cadastrado com sucesso'

class ManuaisDeleteView(DeleteView):
	model = RevisaoManuais 
	pk_url_kwarg = 'pk'
	template_name = 'manuais/manual-delete.html'
	success_url = reverse_lazy('manuais')
	success_message = 'O manual foi deletado com sucesso'

class ManuaisUpdateView(UpdateView):
    model = RevisaoManuais
    form_class = RevisaomanualForm
    template_name = 'manuais/manual-alterar.html'
    context_object_name = 'manuais_list' 
    success_url = reverse_lazy('manuais')
    success_message = 'As alterações foram efectuadas com sucesso'

class ManuaisListView(ListView):
	model = RevisaoManuais
	template_name = 'manuais/manuais.html'
	context_object_name = 'manuais_list' 
	def get_queryset(self):  
		return RevisaoManuais.objects.filter(nome_equipamento_id=self.kwargs['pk'])