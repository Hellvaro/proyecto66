from django import forms
from apps.appmusicoenvivo.models import Banda,Local,Musico
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class bandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = [
            'usuario',
            'comuna',
            'estilo',
            'musicos',
            'nombreBanda',
            'descripcionBanda',
            'miembros',
            'anioFormacion',
            'historia',
            'discografia',
            'imagenBanda',
            'videoBanda',
            'contacto',
        ]
        labels ={
            'usuario':'Usuario',
            'comuna':'Comuna',
            'estilo':'Estilo',
            'musicos':'¿Buscas musico?',
            'nombreBanda':'Nombre',
            'descripcionBanda': 'Descripcion',
            'miembros':'Miembros',
            'anioFormacion':'Año Formación',
            'historia':'Historia',
            'discografia':'Discografia',
            'imagenBanda':'Imagen de Banda',
            'videoBanda':'Link Video',
            'contacto':'Contacto',
        }
        widgets={
            'usuario':forms.HiddenInput(),

        }
        help_texts={
            'musicos': 'Mantenga pulsado Ctrl y click para seleccionar mas de uno',
            'estilo': 'Mantenga pulsado Ctrl y click para seleccionar mas de uno',
            'contacto': 'Email, Whatsapp, Telefono, etc.',
        }


class musicoForm(forms.ModelForm):
    class Meta:
        model = Musico

        fields= [
            'usuario',
            'instrumento',
            'comuna',
            'estilo',
            'nombreMusico',
            'apellido',
            'expFormacion',
            'dispEnsayo',
            'dispConciertos',
            'dispInmediata',
            'equipado',
            'descripcionEquipo',
            'contacto',
            'aniosExperiencia',
            'descripcionPersonal',
            'imagenMusico',
            'videoMusico',
            'influencias',
            'buscaBanda',
            'clasesParticulares',
        ]
        labels={
            'usuario':'Nombre Usuario',
            'instrumento':'Instrumento',
            'comuna':'Comuna',
            'estilo':'Estilo Musical',
            'nombreMusico':'Nombre',
            'apellido':'Apellido',
            'expFormacion':'Formacion Musical y Experiencia',
            'dispEnsayo':'Disponibilidad Ensayo',
            'dispConciertos':'Disponibilidad Conciertos',
            'dispInmediata':'Disponibilidad Inmediata',
            'equipado':'Equipado',
            'descripcionEquipo':'Descripcion Equipo',
            'contacto':'Contacto',
            'aniosExperiencia':'Años de Experiencia',
            'descripcionPersonal':'Descripcion Personal',
            'imagenMusico':'Imagen Musico',
            'videoMusico':'Link Video',
            'influencias':'Influencias Musicales',
            'buscaBanda':'¿Buscas Banda?',
            'clasesParticulares':'¿Realizas clases particulares?',
        }

        widgets = {
            'usuario': forms.HiddenInput(),
            'descripcionEquipo':forms.Textarea(attrs={'placeholder':'Describa los instrumentos y accesorios que posee'})

        }

        help_texts={
            'instrumento':'Mantenga pulsado Ctrl y click para seleccionar mas de uno',
            'estilo':'Mantenga pulsado Ctrl y click para seleccionar mas de uno',
            'contacto': 'Email, Whatsapp, Telefono, etc.',
            'dispEnsayo':'Horas y dias de la semana que puedes ensayar.',
            'dispConciertos':'Horas y dias de la semana que puedes realizar presentaciones en vivo.',
        }


class localForm(forms.ModelForm):
    class Meta:
        model = Local
        fields=[
            'usuario',
            'tipo_Local',
            'comuna',
            'nombreLocal',
            'descripcion',
            'imagenLocal',
            'contacto',
            'buscaBanda',
            'buscaMusico',
            'horarios',
        ]
        labels={
            'usuario':'Nombre Usuario',
            'tipo_Local':'Tipo de Local',
            'comuna':'Comuna',
            'nombreLocal':'Nombre Local',
            'descripcion':'Descripcion',
            'imagenLocal':'Imagen del Local',
            'contacto':'Contacto',
            'buscaBanda':'¿Buscas Bandas para shows en vivo?',
            'buscaMusico':'¿Buscas Musicos para shows en vivo?',
            'horarios':'Horarios',
        }
        widgets = {
            'usuario': forms.HiddenInput(),
        }
        help_texts = {
            'contacto': 'Email, Whatsapp, Telefono, etc.',

        }
class registroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]

        labels={
            'username':'Nombre Usuario',
            'email':'Email',
        }
class contactoForm(forms.Form):

    email = forms.EmailField(max_length=100, label='Tu Correo electronico')
    mensaje = forms.CharField(widget= forms.Textarea)




