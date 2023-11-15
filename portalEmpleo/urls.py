from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.logUser, name='login'),
    path('outUser/', views.outUser, name='logout'),
    path('createUser/', views.createUser, name='createUser'),
    path('createUserEmpresa/', views.createUserEmpresa, name='createUserEmpresa'),
    path('crearOfertas/', views.crearOfertas, name='crearOferta')
]