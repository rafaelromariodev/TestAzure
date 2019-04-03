from django.db import models

# Create your models here.

class Raza(models.Model):
    id = models.IntegerField(primary_key=True)
    raza = models.CharField(max_length=30)
    observaciones = models.TextField(max_length=1000)

    def __str__(self):
        return self.raza

    class Meta:
        managed = False
        db_table = "Raza"
