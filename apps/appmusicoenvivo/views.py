from django.shortcuts import render, render_to_response, redirect, get_object_or_404,HttpResponseRedirect
from apps.appmusicoenvivo.form import bandaForm,musicoForm,localForm
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.appmusicoenvivo.form import registroForm, contactoForm
from django.views.generic import ListView, UpdateView, DeleteView
from apps.appmusicoenvivo.models import Banda,Local,Musico, Region, Comuna
from django.core.mail import EmailMessage
from .filters import BandaFilter, MusicoFilter, LocalFilter



# Create your views here.

class index(ListView):
    template_name = 'appmusicoenvivo/index.html'
    context_object_name = 'usuario'
    model = User
    paginate_by = 3
    # def get_queryset(self, *args,**kwargs):
    #     return Banda.objects.filter()
    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        context.update({
            'bandabenef':Banda.objects.filter(beneficio1=True)[:2],
            'musicobenef':Musico.objects.filter(beneficio1=True).order_by('?')[:1],
            'totalbandas': Banda.objects.all(),
            'totalmusicos':Musico.objects.all(),
            'totallocales':Local.objects.all(),
            'musicos':Musico.objects.all()[:3],
            'locales':Local.objects.all()[:3],
            'bandas':Banda.objects.all()[:3],
            'usuarios':User.objects.all(),

        })
        return context

    # def get_queryset(self, *args, **kwargs):
    #         supermusico = Musico.objects.filter(usuario = self.request.user)
    #         match = Musico.objects.filter(comuna= supermusico.comuna).filter(estilo= supermusico.estilo).filter(buscaBanda=True).filter(instrumento= -supermusico.instrumento)
    #         return match
# def logout(request):
#     logout(request)
#     return redirect('login')
class donaciones(ListView):
    model = User
    template_name = 'appmusicoenvivo/donaciones.html'

class servicios(ListView):
    model = User
    template_name = 'appmusicoenvivo/servicios.html'

def registroExitoso(request):
    return render_to_response('appmusicoenvivo/registroExitoso.html')

def busqueda(request):
    return render_to_response('appmusicoenvivo/Busqueda.html')

def contacto(request):
    if request.method == 'POST':
        formulario = contactoForm(request.POST)
        if formulario.is_valid():
            asunto = 'Mensaje de Usuario'
            mensaje = formulario.cleaned_data['mensaje'] +"\n"
            mensaje += 'Comunicarse a: ' + formulario.cleaned_data['email']
            mail = EmailMessage(asunto,mensaje, to=['musicoenvivo66@gmail.com'])
            mail.send()
        return HttpResponseRedirect('/')
    else:
        formulario = contactoForm()
    return render(request,'appmusicoenvivo/contacto.html', {'formulario':formulario})

class perfilExitoso(ListView):
    template_name = 'appmusicoenvivo/perfilExitoso.html'
    model = User


#----- Usuario ------
class menuUsuario(ListView):
    template_name = 'appmusicoenvivo/menuUsuario.html'
    model = User

class registroUsuario(CreateView):
    model = User
    template_name = "appmusicoenvivo/registroUsuario.html"
    form_class = registroForm
    success_url = reverse_lazy('registroexitoso')
'''
def menuUsuario(request):
    return  render_to_response('appmusicoenvivo/menuUsuario.html',)
'''
class userUpdate(UpdateView):
    model = User
    form_class = registroForm
    template_name = 'appmusicoenvivo/registroUsuario.html'
    success_url = reverse_lazy ('menuUsuario')


#----- Banda ------
def formularioBanda(request,id=None):
    if request.method == 'POST':
        form = bandaForm(request.POST, request.FILES or None)

        if form.is_valid():
            variable = form.save()
            variable.usuario = request.user
            variable.save()
            return redirect('perfilexitoso')
    else:
        form= bandaForm()
    return render(request,'appmusicoenvivo/crearBanda.html', {'form':form},)



def searchB(request):
    banda_list = Banda.objects.all()
    banda_filter = BandaFilter(request.GET, queryset=banda_list)

    return render(request, 'appmusicoenvivo/searchB.html', {'filter': banda_filter,'total':banda_list})

class bandaList(ListView):
    model = Banda
    template_name = 'appmusicoenvivo/bandas.html'
    paginate_by = 2

class bandasPerfil(ListView):
    model = Banda
    template_name = 'appmusicoenvivo/perfilBanda.html'

    def get_queryset(self,*args,**kwargs):
        return Banda.objects.filter(usuario = self.request.user)

class bandaUpdate(UpdateView):
    model = Banda
    form_class = bandaForm
    template_name = 'appmusicoenvivo/crearBanda.html'
    success_url = reverse_lazy ('menuUsuario')

class bandaDelete(DeleteView):
    model = Banda
    template_name = 'appmusicoenvivo/eliminarBanda.html'
    success_url = reverse_lazy('perfilbanda')

def bandaDetalle(request, id=None):
    banda = get_object_or_404(Banda,id=id)

    return render(request,'appmusicoenvivo/detalleBanda.html',{'banda':banda})



#----- Musico ------

def formularioMusico(request):
    if request.method == 'POST':
        form = musicoForm(request.POST, request.FILES or None)
        if form.is_valid():
            variable = form.save()
            variable.usuario = request.user
            variable.save()
            return redirect('perfilexitoso')
    else:
        form= musicoForm()
    return render(request,'appmusicoenvivo/crearMusico.html', {'form':form},)

class musicoList(ListView):
    model = Musico
    template_name = 'appmusicoenvivo/musicos.html'
    paginate_by = 2

class perfilMusico(ListView):
    template_name = 'appmusicoenvivo/perfilMusico.html'
    model = Musico

    def get_queryset(self,*args,**kwargs):
        return Musico.objects.filter(usuario = self.request.user)

class musicoUpdate(UpdateView):
    model = Musico
    form_class = musicoForm
    template_name = 'appmusicoenvivo/crearMusico.html'
    success_url = reverse_lazy ('perfilmusico')

class musicoDelete(DeleteView):
    model = Musico
    template_name = 'appmusicoenvivo/eliminarMusico.html'
    success_url = reverse_lazy('perfilmusico')

def musicoDetalle(request, id=None):
    musico = get_object_or_404(Musico,id=id)

    return render(request,'appmusicoenvivo/detalleMusico.html',{'musico':musico})

def searchM(request):

    musico_list = Musico.objects.all()
    musico_filter = MusicoFilter(request.GET, queryset=musico_list)


    return render(request, 'appmusicoenvivo/searchM.html', {'filter': musico_filter,'total':musico_list})


#----- Local ------

def formularioLocal(request):
    if request.method == 'POST':
        form = localForm(request.POST, request.FILES or None)
        if form.is_valid():
            variable = form.save()
            variable.usuario = request.user
            variable.save()
            return redirect('perfilexitoso')
    else:
        form= localForm()
    return render(request,'appmusicoenvivo/crearLocal.html', {'form':form},)

class localList(ListView):
    model = Local
    template_name = 'appmusicoenvivo/locales.html'

class perfilLocal(ListView):
    template_name = 'appmusicoenvivo/perfilLocal.html'
    model = Local

    def get_queryset(self,*args,**kwargs):
        return Local.objects.filter(usuario = self.request.user)

class localUpdate(UpdateView):
    model = Local
    form_class = localForm
    template_name = 'appmusicoenvivo/crearLocal.html'
    success_url = reverse_lazy('menuUsuario')

class localDelete(DeleteView):
    model = Local
    template_name = 'appmusicoenvivo/eliminarLocal.html'
    success_url = reverse_lazy('perfillocal')

def localDetalle(request, id=None):
    local = get_object_or_404(Local,id=id)

    return render(request,'appmusicoenvivo/detalleLocal.html',{'local':local})

def searchL(request):
    local_list = Local.objects.all()
    local_filter = LocalFilter(request.GET, queryset=local_list)

    return render(request, 'appmusicoenvivo/searchL.html', {'filter': local_filter,'total':local_list})
