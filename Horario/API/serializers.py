from rest_framework.serializers import ModelSerializer
from Horario.models import *
class Profesorserilizer(ModelSerializer):
    class Meta:
        model=Docente
        fields =['CODD','Names','Escuela']