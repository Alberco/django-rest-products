from django.db import models


# Create your models here.
class BaseModel(models.Model):
    """Model definition for BaseModel."""

    # TODO: Define fields here
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado',default=True)
    created_date = models.DateField('Fecha de creacion',auto_now=False,auto_now_add=True)
    modified_date = models.DateField('Fecha de modificacion',auto_now=True,auto_now_add=False)
    deleted_date = models.DateField('Fecha de eliminacion',auto_now=True,auto_now_add=False)
    
    
    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'