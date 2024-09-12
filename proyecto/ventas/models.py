from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError


class Vendedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="vendedor")
    celular = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatares", blank=True, null=True)

    def __str__(self) -> str:
        return self.usuario.username
    
    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING, related_name='ventas')
    producto = models.ForeignKey("productos.Producto", on_delete=models.DO_NOTHING)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_venta = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ['-fecha_venta']

    def clean(self):
            if not self.producto:
                raise ValidationError('El producto no existe')
            if self.producto.stock == 0:
                raise ValidationError('No hay stock disponible para este producto')
            if self.cantidad > self.producto.stock:
                raise ValidationError(
                    f'No hay suficiente stock disponible para vender {self.cantidad} unidades.'
                    f'Solo hay {self.producto.stock} unidades disponibles.'
                )

    def save(self, *args, **kwargs):
        self.precio_total = self.producto.precio * self.cantidad
        self.producto.disminuir_stock(self.cantidad)
        super().save(*args, **kwargs)