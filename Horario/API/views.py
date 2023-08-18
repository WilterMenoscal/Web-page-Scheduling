from rest_framework.viewsets import ModelViewSet
from Horario.models import *
from Horario.API.serializers import *

class ProfesorApiViewSet(ModelViewSet):
    serializer_class = Profesorserilizer
    queryset = Docente.objects.all()