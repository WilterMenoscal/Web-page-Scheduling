from django.db import models

# Create your models here.
class Escuela(models.Model):
    id=models.AutoField(primary_key=True)
    NSchool= models.CharField(max_length=50)
    NCarrera= models.CharField(max_length=50)
    def __str__(self):
        texto="{0}({1})"
        return texto.format(self.NSchool,self.NCarrera)
class Docente(models.Model):
    id=models.AutoField(primary_key=True)
    CODD= models.CharField(unique=True,max_length=20)
    Names= models.CharField(null=True,max_length=50)
    D_Escuela= models.ForeignKey(Escuela,on_delete=models.CASCADE)
    def __str__(self):
        texto="{0}({1})"
        return texto.format(self.Names,self.D_Escuela)

class Materia(models.Model):
    COD = models.CharField(unique=True,max_length=50, verbose_name="Code")
    Materia = models.CharField(max_length=50, verbose_name="Subject")
    M_Escuela = models.ForeignKey(Escuela,on_delete=models.CASCADE)
    semestre = models.CharField(max_length=50, verbose_name="Semester")
    Cupos = models.IntegerField(verbose_name="Space")
    CODDO = models.ForeignKey(Docente, on_delete=models.CASCADE)
    def __str__(self):
        texto="{0}({1})"
        return texto.format(self.COD,self.Materia)


class Aula(models.Model):
    CODA= models.CharField(max_length=50)
    Subject_id= models.ForeignKey(Materia,verbose_name='Subject',on_delete=models.CASCADE)
    cupoA= models.IntegerField(null=True,verbose_name='Cupos')
    ocupdia= models.CharField(null=True,max_length=50)
    start=models.CharField(null=True,max_length=50)
    end=models.CharField(null=True,max_length=50)