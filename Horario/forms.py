from django.forms import *
from Horario.models import *
from django.forms import *
class profesorforms(ModelForm):
    class Meta:
        model=Docente
        fields='__all__'
class materiaforms(ModelForm):
    class Meta:
        model=Materia
        fields='__all__'
        widgets={
            'COD':TextInput(
            attrs={
                'Code':'form-control'
            }
            ),
        }
class aulaforms(ModelForm):
    class Meta:
        model=Aula
        fields='__all__'
