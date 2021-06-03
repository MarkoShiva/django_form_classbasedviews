from django import forms
from manuais.models import Equipamentos, RevisaoManuais

# Forms do Revisão Manual
class EquipamentosForm(forms.ModelForm):
    class Meta:
        model = Equipamentos
        fields = '__all__'

# Forms do Revisão Manual
class RevisaomanualForm(forms.ModelForm):
    class Meta:
        model = RevisaoManuais
        fields = '__all__'