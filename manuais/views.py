from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.base import TemplateView

from manuais.forms import EquipamentosForm, RevisaomanualForm
from manuais.models import Equipamentos, RevisaoManuais


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
	model = RevisaoManuais
	# fields = '__all__'

	

	def get_success_url(self) -> str:
		messages.success(self.request, 'Manual Cadastrado com sucesso')
		return reverse_lazy('equipamentos')

class ManuaisDeleteView(DeleteView):
	model = RevisaoManuais 
	# pk_url_kwarg = 'pk'
	template_name = 'manuais/manual-delete.html'
	# success_url = reverse_lazy('manuais')
	# success_message = 'O manual foi deletado com sucesso'

	def get_success_url(self):
		messages.success(self.request, 'O manual foi deletado com sucesso')
		return reverse_lazy('manuais', kwargs = {'pk': self.object.nome_equipamento.id })

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
