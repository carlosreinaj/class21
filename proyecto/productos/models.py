from django.db import models

class ProductosCategoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Categoria de Producto'
        verbose_name_plural = 'Categorias de Productos'

class Producto(models.Model):
    categoria = models.ForeignKey(ProductosCategoria, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    #Como hacer para categoria y nombre sean unicos?
    descripcion = models.TextField(blank=True, null=True)
    unidad_de_medida = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.FloatField()
    fecha_actualizacion = models.DateField(editable=False, auto_now=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.unidad_de_medida} ${self.precio: 2f})"
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        # La siguiente línea es para que no se puedan repetir el nombre y la categoría
        constraints = [
            models.UniqueConstraint(fields=['categoria', 'nombre'], name='categoria_nombre')
        ]
        # La siguiente línea es para crear un índice en la base de datos
        # Un ínidice es una estructura de datos que mejora la velocidad de búsqueda
        indexes = [models.Index(fields=['nombre'])]

    def disminuir_stock(self, cantidad):
        """cantidad es enviado desde el modelo Venta"""
        if self.stock >= cantidad:
            self.stock -= cantidad
            self.save()
        else:
            raise ValueError('No hay suficiente stock disponible')

    def aumentar_stock(self, cantidad):
        self.stock += cantidad
        self.save()