from django.db import models
# Create your models here.

class Form(models.Model):
    name = models.CharField("Имя", max_length=50)
    email = models.CharField("Почта", max_length=254)
    
    class Meta:
        verbose_name = 'Имя',
        verbose_name_plural = 'Имена '
        
        
    def __str__(self):
        return self.name    
    
