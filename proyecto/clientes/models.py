from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre
    
    class Meta: 
        verbose_name = "Pais de origen"
        verbose_name_plural = "Paises de origen"
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Pais de origen')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
