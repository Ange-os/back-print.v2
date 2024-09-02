from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.hashers import check_password, make_password


# Create your models here.

#Modelos

class Users(models.Model):
    userName = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=128)
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk or not check_password(self.password, self.password):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.userName

class Project(models.Model):
    name_project = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='proyectos')
    
    def __str__(self):
        return self.name_project

class Template(models.Model):
    name_template = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='templates')
    
    def __str__(self):
        return self.name_template

class Layer(models.Model):
    LAYER_TYPES = (
        ('TEXT', 'Texto'),
        ('IMAGE', 'Imagen'),
        ('SHAPE', 'Forma'),
        ('FILTRO', 'Filtro'),
        # Otros tipos de capas que consideres necesarios
    )
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='layers')
    layer_type = models.CharField(max_length=10, choices=LAYER_TYPES)
    content = models.TextField()  # Puede ser un texto, una URL a una imagen, etc.
    position = models.JSONField()  # Para almacenar la posición en el canvas (x, y, z)
    size = models.JSONField()  # Tamaño de la capa (ancho, alto)
    
    def __str__(self):
        return f"{self.layer_type} - {self.project.name_project}"

class Asset(models.Model):
    name_asset = models.CharField(max_length=100)
    file = models.FileField(upload_to='assets/')
    uploaded_at = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='assets', null=True, blank=True)  # Relación con Project
    layer = models.ForeignKey(Layer, on_delete=models.CASCADE, related_name='assets', null=True, blank=True)  # Relación con Layer
    
    def __str__(self):
        return self.name_asset        