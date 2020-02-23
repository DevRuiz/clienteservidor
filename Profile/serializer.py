from rest_framework import routers, serializers, viewsets

from Profile.models import Profile
from Profile.models import Genero
from Profile.models import Ocupacion
from Profile.models import Estado
from Profile.models import Ciudad
from Profile.models import EstadoCivil


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')

class GeneroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('__all__')
        

class OcupacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ocupacion
        fields = ('__all__')

class EstadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = fields = ('__all__')

class CiudadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('__all__')

class EstadoCivilSerializers(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = ('__all__')


        