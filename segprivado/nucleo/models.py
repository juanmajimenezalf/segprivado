from django.db import models

# Create your models here.
class Medico(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellidos = models.CharField(max_length=50, verbose_name="Apellidos")
    edad = models.IntegerField(verbose_name="Edad")
    fechaalta = models.DateTimeField(verbose_name="Fecha de alta")
    especialidad = models.Choices([('MF', 'Medico de Familia'), ('Dig', 'Digestivo'), ('Neuro', 'Neurologo'), ('Derma', 'Dermatologo'), ('Trauma', 'Traumatologo'),], verbose_name="Especialidad")
    username = models.CharField(max_length=30, verbose_name="Usuario")
    password = models.CharField(max_length=30, verbose_name="Contraseña")
    
class Paciente(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellidos = models.CharField(max_length=50, verbose_name="Apellidos")
    edad = models.IntegerField(verbose_name="Edad")
    direccion = models.CharField(max_length=100, verbose_name="Direccion")
    foto = models.ImageField(upload_to='fotos', verbose_name="Foto")
    username = models.CharField(max_length=30, verbose_name="Usuario")
    password = models.CharField(max_length=30, verbose_name="Contraseña")
    
class Cita(models.Model):
    fecha = models.DateTimeField(verbose_name="Fecha")
    observaciones = models.TextField(max_length=200, verbose_name="Observaciones")
    idMedico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name="Medico")
    idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    
class Medicamento(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    descripcion = models.TextField(max_length=100, verbose_name="Descripcion")
    receta = models.CharField(max_length=1, verbose_name="Receta")
    precio = models.FloatField(verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock")
    
class Compra(models.Model):
    fecha = models.DateTimeField(verbose_name="Fecha")
    idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    precio = models.FloatField(verbose_name="Precio")
    
class Compra_medicamento(models.Model):
    idCompra = models.ForeignKey(Compra, on_delete=models.CASCADE, verbose_name="Compra")
    idMedicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, verbose_name="Medicamento")
    