from django.shortcuts import render

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

import coreapi
from rest_framework.schemas import AutoSchema


#Importar el modelo
from Profile.models import Profile
from Profile.models import Genero
from Profile.models import Ocupacion
from Profile.models import Estado
from Profile.models import Ciudad
from Profile.models import EstadoCivil

#Importar los Serializers
from Profile.serializer import ProfileSerializers
from Profile.serializer import GeneroSerializers
from Profile.serializer import OcupacionSerializers
from Profile.serializer import EstadoSerializers
from Profile.serializer import CiudadSerializers
from Profile.serializer import EstadoCivilSerializers

class ListAutoSchema(AutoSchema):
    def get_manual_fields(self,path, method):
        extra_fields = []
        if method.lower() in ('post', 'get'):
            extra_fields = [

                coreapi.Field('nombre'),
                coreapi.Field('apePat'),
                coreapi.Field('apeMat'),
                coreapi.Field('edad'),
                coreapi.Field('ciudad_id'),
                coreapi.Field('genero_id'),
                coreapi.Field('ocupacion_id'),
                coreapi.Field('estado_id'),
                coreapi.Field('estadoCivil_id'),

            ]
        manual_fields = super().get_manual_fields(path,method)
        return manual_fields + extra_fields

class ProfileList(APIView):
    #METODO GET PARA SOLICTAR INFO
    permission_classes = []
    schema = ListAutoSchema()
    def get(self, request, format = None):
        print("Metodo get filter")
        queryset = Profile.objects.filter(delete = False)
        #many = True si aplica si retorno multiples objetos
        serializer = ProfileSerializers(queryset, many = True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = ProfileSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class GeneroAutoShema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post', 'get'):
            extra_fields = [
                coreapi.Field('genero'),
            ]
        manual_fields= super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class GeneroList(APIView):
    #METODO GET PARA SOLICTAR INFO
    permission_classes = []
    schema = GeneroAutoShema()
    def get(self, request, format = None):
        print("Metodo get filter")
        queryset = Genero.objects.filter(delete = False)
        #many = True si aplica si retorno multiples objetos
        serializer = GeneroSerializers(queryset, many = True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = GeneroSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OcupacionAutoSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post', 'get'):
            extra_fields = [
                coreapi.Field('ocupacion'),
            ]
        manual_fields= super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class OcupacionList(APIView):
    #METODO GET PARA SOLICTAR INFO
    permission_classes = []
    schema = OcupacionAutoSchema()
    def get(self, request, format = None):
        print("Metodo get filter")
        queryset = Ocupacion.objects.filter(delete = False)
        #many = True si aplica si retorno multiples objetos
        serializer = OcupacionSerializers(queryset, many = True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = OcupacionSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoAutoSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post', 'get'):
            extra_fields = [
                coreapi.Field('estado'),
            ]
        manual_fields= super().get_manual_fields(path, method)
        return manual_fields + extra_fields

class EstadoList(APIView):
    #METODO GET PARA SOLICTAR INFO
    permission_classes = []
    schema = EstadoAutoSchema()
    def get(self, request, format = None):
        print("Metodo get filter")
        queryset = Estado.objects.filter(delete = False)
        #many = True si aplica si retorno multiples objetos
        serializer = EstadoSerializers(queryset, many = True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = EstadoSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CiudadAutoSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post', 'get'):
            extra_fields = [
                coreapi.Field('ciudad'),
                coreapi.Field('estado_id'),
            ]
        manual_fields= super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class CiudadList(APIView):
    #METODO GET PARA SOLICTAR INFO
    permission_classes = []
    schema = CiudadAutoSchema()
    def get(self, request, format = None):
        print("Metodo get filter")
        queryset = Ciudad.objects.filter(delete = False)
        #many = True si aplica si retorno multiples objetos
        serializer = CiudadSerializers(queryset, many = True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = CiudadSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoCivilAutoSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ('post', 'get'):
            extra_fields = [
                coreapi.Field('estadoCivil'),
            ]
        manual_fields= super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class EstadoCivilList(APIView):
    #METODO GET PARA SOLICTAR INFO
    permission_classes = []
    schema = EstadoCivilAutoSchema()
    def get(self, request, format = None):
        print("Metodo get filter")
        queryset = EstadoCivil.objects.filter(delete = False)
        #many = True si aplica si retorno multiples objetos
        serializer = EstadoCivilSerializers(queryset, many = True)
        return Response(serializer.data)

    def post(self,request, format = None):
        serializer = EstadoCivilSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


