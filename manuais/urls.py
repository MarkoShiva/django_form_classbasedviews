from django.urls import path, re_path

from manuais.views import (EquipamentosDeleteView, EquipamentosIndexView,
                           EquipamentosListView, EquipamentosNewView,
                           EquipamentosUpdateView, ManuaisDeleteView,
                           ManuaisIndexView, ManuaisListView, ManuaisNewView,
                           ManuaisUpdateView)

# app_name = "equipment"

urlpatterns = [
	path('', EquipamentosIndexView.as_view(), name='index-equipamentos'),
	path('equipamentos/', EquipamentosListView.as_view(), name='equipamentos'), 
	path('Equipamento-novo/', EquipamentosNewView.as_view(), name='equipoamento-novo'),
	path('<int:pk>/alterar/', EquipamentosUpdateView.as_view(), name='equipamento-alterar'),
	path('<int:pk>/delete/', EquipamentosDeleteView.as_view(), name='equipamento-delete'), 

	path('', ManuaisIndexView.as_view(), name='index-manuais'),
	path('equipamentos/<int:pk>/', ManuaisListView.as_view(), name='manuais'), 
	path('manual-novo/', ManuaisNewView.as_view(), name='manual-novo'), 
	path('alterar/<int:pk>/', ManuaisUpdateView.as_view(), name='manual-alterar'),
	path('delete/<int:pk>', ManuaisDeleteView.as_view(), name='manual-delete'),  
]
