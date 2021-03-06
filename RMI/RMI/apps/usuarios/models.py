#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
from django.conf import settings
import os

from django.db import models

SUPERVISOR=(
	('Julio Prado','Julio Prado '),
	('Maria del Carmen','Maria del Carmen'),
	('Janeth Patricia','Janeth Patricia'),
	('No tiene','No tiene'),
	)

class User_profile(models.Model):	

	user     = models.OneToOneField(User)	
	telefono = models.CharField(max_length=13)
	supervisor = models.CharField(max_length=50, choices = SUPERVISOR,default='')
	enero = models.BooleanField(default=False)
	febrero = models.BooleanField(default=False)
	marzo = models.BooleanField(default=False)
	abril = models.BooleanField(default=False)
	mayo = models.BooleanField(default=False)
	junio = models.BooleanField(default=False)
	julio = models.BooleanField(default=False)
	agosto = models.BooleanField(default=False)
	septiembre = models.BooleanField(default=False)
	octubre = models.BooleanField(default=False)
	noviembre = models.BooleanField(default=False)
	diciembre = models.BooleanField(default=False)

	
	def __unicode__(self):
		return "Nombre: %s %s; Cedula: %s" % (self.user.first_name, self.user.last_name, self.user.username)
#		
class Reporte_Mensual(models.Model):

	mes = models.CharField(max_length= 30)
	nombre_adjunto = models.CharField(max_length= 50)
	adjunto_exel = models.FileField(upload_to='Informe/')	
	usuario = models.ForeignKey(User)
	fecha = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return "MES: %s; NOMBRE ADJUNTO: %s; USUARIO: %s %s"  % (self.mes, self.nombre_adjunto, self.usuario.first_name , self.usuario.last_name)

@receiver(pre_delete, sender=Reporte_Mensual)
def _Reporte_Mensual_delete(sender, instance, using, **kwargs):	
    file_path = settings.MEDIA_ROOT + str(instance.adjunto_exel)
    #print(file_path)

    if os.path.isfile(file_path):
        os.remove(file_path)	
     