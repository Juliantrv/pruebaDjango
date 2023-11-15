from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.conf import settings
from . import forms, models

# Create your views here
def home(request):
    ofertas = models.Oferta.objects.all()
    return render(request, 'home.html', {
        'ofertas': ofertas
    })

# REGISTRO DE USUARIO
def createUser(request):
    error = ''

    try:
        if request.method == 'POST':
            if request.POST['password1'] == request.POST['password2']:
                try:
                    # print(request.POST)
                    user = User.objects.create_user(
                        username=request.POST['username'],
                        password=request.POST['password1'],
                        email=request.POST['email'],
                        first_name=request.POST['nombres'],
                        last_name=request.POST['apellidos']
                    )
                    user.save()
                    usuario = models.Usuario.objects.create(
                        fecha_nacimiento=request.POST['fecha_nacimiento'],
                        profesion=request.POST['profesion'],
                        descripcion_perfil=request.POST['descripcion_perfil'],
                        numero_identificacion=request.POST['numero_identificacion'],
                        celular=request.POST['celular'],
                        user=user
                    )
                    usuario.save()

                    subject = 'Registro exitoso'
                    message = 'El registro de usuario se a realizo con exito'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [request.POST['email']]
                    send_mail(subject, message, email_from, recipient_list)

                    error = 'El registro de usuario se a realizo con exito, a su correo le llegar un mensaje de confirmación'

                    login(request, user)
                except:
                    error = 'Username already exists'
            else:
                error = 'Password do not match'
    except:
        error = 'Ingrese datos validos'

    return render(request, 'createUser.html', {
        'form': UserCreationForm,
        'infoUsuario': forms.UsuarioForm,
        'error': error
    })

# REGISTRO DE USUARIO EMPRESA
def createUserEmpresa(request):
    error = ''

    try:
        if request.method == 'POST':
            if request.POST['password1'] == request.POST['password2']:
                try:
                    print(request.POST)
                    user = User.objects.create_user(
                        username=request.POST['username'],
                        password=request.POST['password1'],
                        email=request.POST['email']
                    )
                    user.save()
                    empresa = models.Empresa.objects.create(
                        nombre=request.POST['nombre'],
                        nit=request.POST['nit'],
                        descripcion=request.POST['descripcion'],
                        user=user
                    )
                    empresa.save()

                    subject = 'Registro exitoso'
                    message = 'El registro de Empresa se a realizo con exito'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [request.POST['email']]
                    send_mail(subject, message, email_from, recipient_list)

                    error = 'El registro de Empresa se a realizo con exito, a su correo corporativo le llegar un mensaje de confirmación'

                    login(request, empresa)
                except:
                    error = 'Username already exists'
            else:
                error = 'Password do not match'
    except:
        error = 'Ingrese datos validos'

    return render(request, 'createUserEmpresa.html', {
        'form': UserCreationForm,
        'infoUsuario': forms.EmpresaForm,
        'error': error
    })

# LOGIN
def logUser(request):

    error = ''
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            error = 'User or password is incorrect'
        else:
            login(request, user)
            return redirect('home')
    return render(request, 'loguser.html', {
        'form': AuthenticationForm,
        'error': error
    })

# LOGOUT
def outUser(request):

    logout(request)
    return redirect('home')

# CREAR_OFERTAS
def crearOfertas(request):

    error = ''
    if request.method == 'POST':
        try:
            oferta = models.Oferta.objects.create(
                titulo = request.POST['titulo'],
                descripcion = request.POST['descripcion'],
                salario = request.POST['salario'],
                habiliadades = request.POST['habiliadades']
            )
            oferta.save()
        except:
            error = 'No se pudo crear la oferta de trabajo, contacte con el proveedor'
    return render(request, 'crearOfertas.html', {
        'form': forms.OfertaForm,
        'error': error
    })
