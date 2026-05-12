from django.db import models

# Create your models here.
class Guild(models.Model):
    name = models.CharField(max_length=100, unique=True)
    kingdom = models.CharField(max_length=100)
    max_capacity = models.IntegerField(default=50)

    def __str__(self):
        return f"{self.name} ({self.kingdom}) - Capacity: {self.max_capacity}"
    
class Adventurer(models.Model):
    
    CLASS_CHOICES = [
        ('MAGE', 'Mago'), 
        ('WARRIOR', 'Guerrero'), 
        ('ROGUE', 'Pícaro'), 
        ('CLERIC', 'Clérigo'), 
        ('RANGER', 'Explorador'),
    ]

    STATUS_CHOICES = [
        ('ACTIVE', 'Activo'),
        ('MISSION', 'En misión'),
        ('DEAD', 'MUERTO'),
    ]

    name = models.CharField(max_length=100)
    class_type = models.CharField(max_length=20, choices=CLASS_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    level = models.IntegerField(default=1)
    guild = models.ForeignKey(Guild, related_name='adventurers', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.class_type} (Nivel {self.level}) - {self.status}"