from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Productos(models.Model):
    id_producto = models.IntegerField(primary_key=True, default=1, 
                    validators=[MaxValueValidator(100), MinValueValidator(1)])
    nombre_producto = models.CharField(max_length=60)
    stock_producto = models.IntegerField(default=1, 
                    validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __str__(self):
        return self.nombre_producto



