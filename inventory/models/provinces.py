from django.db import models

#26 Provinces de la RDC
class Province(models.Model):
    name = models.fields.CharField(max_length=150)
    chef_lieu = models.fields.CharField(null=True, max_length=150)
    superficie= models.fields.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    population = models.fields.IntegerField(blank=True, null=True) 
    rank =  models.fields.CharField(max_length=150, blank=True, null=True)
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name