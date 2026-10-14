from django.db import models

# Create your models here.
class cliente(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class atencion(models.Model):
    id_atencion = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Atención {self.id_atencion} - {self.cliente.nombre} {self.cliente.apellido}"