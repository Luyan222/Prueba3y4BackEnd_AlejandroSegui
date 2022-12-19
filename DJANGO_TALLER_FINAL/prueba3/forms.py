from django import forms
from prueba3.models import Inscritos

class FormInscritos(forms.ModelForm):
    class Meta:
        model = Inscritos
        fields = '__all__'

