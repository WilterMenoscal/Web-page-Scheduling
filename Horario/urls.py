from django.urls import path
from Horario.views import *

urlpatterns = [
    path('calendar/', calendarview, name='calendar'),
    path('createprofesor/', createprofCreateView.as_view(), name='create_profesor'),
    path('createprofesor/edicionDocente/<codigo>', edicionDocente),
    path('createprofesor/editarDocente/', editarDocente),
    path('createprofesor/eliminarDocente/<codigo>', eliminarDocente),
    path('createaula/', create_aula, name='create_aula'),
    path('createaula/edicionAula/<codigo>', edicionAula),
    path('createaula/editarAula/', editarAula),
    path('createaula/eliminarAula/<codigo><day><subject>', eliminarAula),
    path('createsubject/', creatematCreateView.as_view(), name='create_subject'),
    path('createsubject/edicionMateria/<codigo>', edicionMateria),
    path('createsubject/editarMateria/', editarMateria),
    path('createsubject/eliminarMateria/<codigo>', eliminarMateria),
    path('contact/',contact, name='contact'),
    path('home/', index, name='index'),
    path('login/', index, name='login'),
    path('register/', index, name='register'),
    path('base/', index, name='base')
]
