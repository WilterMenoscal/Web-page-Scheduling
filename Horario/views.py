import django.http
from django.shortcuts import render, redirect
from Horario.models import *
from django.contrib import messages
from django.views.generic import ListView, CreateView
from Horario.forms import *
from django.urls import reverse_lazy
from django.http import *
def edicionMateria(request, codigo):
    materia = Materia.objects.get(COD=codigo)
    return render(request, "edicionm.html", {"materia": materia})

def editarMateria(request):
    codigo = request.POST['txtCodigo']
    materianom = request.POST['txtNombre']
    carrera = request.POST['carrera']
    semestre = request.POST['semestre']
    cupos =request.POST['cupo']
    coddo=request.POST['coddo']
    materia = Materia.objects.get(COD=codigo)
    materia.Materia = materianom
    materia.semestre=semestre
    materia.Cupos=cupos
    materia.save()

    messages.success(request, '¡Curso actualizado!')

    return redirect('/home/createsubject/')

def eliminarMateria(request, codigo):
    materia = Materia.objects.get(COD=codigo)
    materia.delete()

    messages.success(request, '¡Curso eliminado!')

    return redirect('/home/createsubject/')

def edicionDocente(request, codigo):
    curso = Docente.objects.get(CODD=codigo)
    return render(request, "edicionp.html", {"curso": curso})

def editarDocente(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    carrera = request.POST['carrera']

    curso = Docente.objects.get(CODD=codigo)
    curso.Names = nombre
    curso.D_Escuela.NSchool = carrera
    curso.save()

    messages.success(request, '¡Curso actualizado!')

    return redirect('/home/createprofesor/')

def eliminarDocente(request, codigo):
    docente = Docente.objects.get(CODD=codigo)
    docente.delete()

    messages.success(request, '¡Curso eliminado!')

    return redirect('/home/createprofesor')

class createprofCreateView(CreateView):
    model = 'Docente'
    form_class = profesorforms
    template_name = 'createProfesor.html'
    success_url = reverse_lazy('create_profesor')
    def get_context_data(self, **kwargs):
        Context=super().get_context_data(**kwargs)
        Context['title']='A new profesor'
        Context['object_list']=Docente.objects.all()
        return Context

class creatematCreateView(CreateView):
    model = 'Materia'
    form_class = materiaforms
    template_name = 'createMateria.html'
    success_url = reverse_lazy('create_subject')
    def get_context_data(self, **kwargs):
        Context=super().get_context_data(**kwargs)
        Context['title']='A new materia'
        Context['object_list']=Materia.objects.all()
        return Context

def edicionAula(request, codigo):
    aula = Aula.objects.get(CODA=codigo)
    return render(request, "ediciona.html", {"aula": aula})

def editarAula(request):

    coda = request.POST['coda']
    subject_id = int(request.POST['subject_id'])
    cupos = int(request.POST['cupos'])
    ocupdia = request.POST['ocupdia']
    start = request.POST['start']
    end = request.POST['end']
    aula=Aula.objects.get(CODA=coda)
    existing_aulas = Aula.objects.filter(CODA=coda, ocupdia=ocupdia, start__lt=end, end__gt=start)
    if existing_aulas.exists():
        return redirect('/home/createsubject/editarAaula/'+coda)
    # Check if the number of cupos of the materia is less than or equal to the input cupos
    materia_cupos = Materia.objects.get(id=subject_id).Cupos
    if materia_cupos <= cupos:
        aula.cupoA = cupos
        aula.ocupdia = ocupdia
        aula.start = start
        aula.end = end
        aula.save()
    messages.success(request, '¡Curso actualizado!')
    return redirect('/home/createaula/')


def eliminarAula(request, codigo, day, Subject):

    messages.success(request, '¡Curso eliminado!')

    return redirect('/home/createaula/')

def create_aula(request):
    if request.method == 'POST':
        coda = request.POST['coda']
        subject_id = int(request.POST['subject_id'])
        cupos = int(request.POST['cupos'])
        ocupdia = request.POST['ocupdia']
        start = request.POST['start']
        end = request.POST['end']

        # Check if the classroom is available at the given day and time
        existing_aulas = Aula.objects.filter(CODA=coda, ocupdia=ocupdia, start__lt=end, end__gt=start)
        if existing_aulas.exists():
            return redirect('create_aula')

        # Check if the number of cupos of the materia is less than or equal to the input cupos
        materia_cupos = Materia.objects.get(id=subject_id).Cupos
        if materia_cupos <= cupos:
            aula = Aula.objects.create(CODA=coda, Subject_id_id=subject_id, cupoA=cupos, ocupdia=ocupdia, start=start, end=end)
            return redirect('create_aula')
        else:
            return redirect('create_aula')

    escuelas = Escuela.objects.all()
    docentes = Docente.objects.all()
    materias = Materia.objects.all()
    aulas = Aula.objects.all()
    context = {'escuelas': escuelas, 'docentes': docentes, 'materias': materias, 'aulas': aulas}
    return render(request, 'createa.html', context)

def createsubject(request):
    return render(request, 'createMateria.html')
def index(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'products.html')
def base(request):
    return render(request, 'base.html')
def contact(request):
    return render(request, 'contact.html')



def calendarview(request):
    data_from_db = Aula.objects.all()

    # Obtener la lista de números de aulas únicos
    aulas = list(set([entry.CODA for entry in data_from_db]))
    materias = list(set([entry.Subject_id.Materia for entry in data_from_db]))
    docentes = list(set([entry.Subject_id.CODDO.Names for entry in data_from_db]))

    filtro_aula = request.GET.get('aula', '')
    filtro_materia = request.GET.get('materia', '')
    filtro_docente = request.GET.get('docente', '')

    # Organizar los datos en una estructura para el DataGrid
    days_of_week = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
    hours_of_day = ['07:00am', '08:00am', '09:00am', '10:00am', '11:00am', '12:00pm', '13:00pm', '14:00pm', '15:00pm', '16:00pm', '17:00pm', '18:00pm', '19:00pm']

    # Crear una estructura de datos para el DataGrid
    datagrid_data = []
    for hour in hours_of_day:
        row = {'hour': hour}
        hourc = hour.replace('am', '').replace('pm', '')
        for day in days_of_week:
            ocupado = False
            materia = ''
            aula = ''
            for entry in data_from_db:
                if entry.ocupdia == day and entry.start <= hourc and entry.end > hourc and (filtro_aula == '' or entry.CODA == filtro_aula) and (filtro_materia == '' or entry.Subject_id.Materia == filtro_materia) and (filtro_docente == '' or entry.Subject_id.CODDO.Names == filtro_docente):
                    ocupado = True
                    materia = entry.Subject_id.Materia
                    docente=entry.Subject_id.CODDO.Names
                    aula = entry.CODA
                    break
            if ocupado:
                row[day] = f'{materia}, Aula:{aula}, Docente:{docente}'
            else:
                row[day] = 'Libre'
        datagrid_data.append(row)
    docente_classes = []
    if filtro_docente:
        for entry in data_from_db:
            if entry.Subject_id.CODDO.Names == filtro_docente:
                docente_classes.append(f'{entry.Subject_id.Materia}, Aula:{entry.CODA}')
    context = {
        'datagrid_data': datagrid_data,
        'aulas': aulas,
        'filtro_aula': filtro_aula,
        'materias': materias,
        'filtro_materia': filtro_materia,
        'docentes': docentes,
        'filtro_docente': filtro_docente,
        'docente_classes': docente_classes,
    }
    return render(request, 'calendar.html',context)
