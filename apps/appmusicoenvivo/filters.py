from django.contrib.auth.models import User
from apps.appmusicoenvivo.models import Banda, Musico, Local
import django_filters
import django_filters as filters
class BandaFilter(django_filters.FilterSet):

    class Meta:
        model = Banda
        fields = ['comuna', 'estilo', 'musicos', ]


class MusicoFilter(django_filters.FilterSet):
    dispInmediata = filters.BooleanFilter(label="Disponibilidad Inmediata", )
    equipado = filters.BooleanFilter(label="Musico con Equipo")
    buscaBanda = filters.BooleanFilter(label='Busca Banda')
    clasesParticulares = filters.BooleanFilter(label='Imparte Clases')

    class Meta:
        model = Musico
        fields = [
            'comuna',
            'estilo',
            'instrumento',
            'dispInmediata',
            'equipado',
            'buscaBanda',
            'clasesParticulares',
        ]

class LocalFilter(django_filters.FilterSet):
    buscaBanda = filters.BooleanFilter(label='Busca Banda')
    buscaMusico = filters.BooleanFilter(label='Busca Musico')


    class Meta:
        model = Local
        fields = [
            'tipo_Local',
            'comuna',
            'buscaBanda',
            'buscaMusico',
        ]
