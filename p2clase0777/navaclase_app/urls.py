from django.urls import path
from . import views

urlpatterns = [
   path('',views.hola, name='navaclase_app'),
   path('cbtis/',views.cbtis,name='cbtis'),
   path('<str:nombre>/',views.alumnos,name='alumnos'),
   

]