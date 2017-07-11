from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class MultiSerializerViewSet(ModelViewSet):
    serializers = {
        'default': None,
    }

    def get_serializer_class(self):
            return self.serializers.get(self.action,
                        self.serializers['default'])

class AlumnoViewSet(MultiSerializerViewSet):
    queryset = Alumno.objects.all()
    serializers = {
        'default':    AlumnoSerializer,
        'create':  AlumnoPostSerializer,
        'retrieve': AlumnoPostSerializer,
        'update': AlumnoPostSerializer,
        # 'destroy': CursoDeleteSerializer
    }

    def get_queryset(self):
        queryset = Alumno.objects.all()
        nombre = self.request.query_params.get('nombre', None)
        apellido = self.request.query_params.get('nombre', None)
        curso = self.request.query_params.get('curso', None)
        numero_doc = self.request.query_params.get('numero_doc', None)
        numero_folio = self.request.query_params.get('numero_folio', None)
        libro_matriz = self.request.query_params.get('libro_matriz', None)
        genero = self.request.query_params.get('genero', None)
        curso_estado = self.request.query_params.get('curso_estado', None)
        
        if nombre is not None:
            queryset = queryset.filter(Q(nombre__contains=curso_nombre) | Q(apellido__contains=curso_nombre))
        if curso is not None:
             queryset = queryset.filter(inscripciones__curso__pk=curso)
        if numero_doc is not None:
            queryset = queryset.filter(numero_doc=numero_doc)
        if numero_folio is not None:
            queryset = queryset.filter(numero_folio=numero_folio)
        if libro_matriz is not None:
            queryset = queryset.filter(libro_matriz=libro_matriz)
        if genero is not None:
            queryset = queryset.filter(genero=genero)
        if curso_estado is not None:
            queryset = queryset.filter(inscripciones__estado=curso_estado)
        return queryset.order_by("apellido")


class CursoViewSet(MultiSerializerViewSet):
    queryset = Curso.objects.all()
    serializers = {
        'default':    CursoSerializer,
        'create':  CursoPostSerializer,
        'retrieve': CursoPostSerializer,
        'update': CursoPostSerializer,
        # 'destroy': CursoDeleteSerializer
    }


    def get_queryset(self):
        queryset = Curso.objects.all()
        plan_id = self.request.query_params.get('planId', None)
        curso_nombre = self.request.query_params.get('cursoNombre', None)

        if curso_nombre is not None:
            queryset = queryset.filter(nombre__contains=curso_nombre)
        if plan_id is not None:
            queryset = queryset.filter(plan_id=plan_id)
        return queryset


class PlanViewSet(ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def get_queryset(self):
        queryset = Plan.objects.all()
        nombre = self.request.query_params.get('nombre', None)

        if nombre is not None:
            queryset = queryset.filter(nombre__contains=nombre)
        return queryset


class MateriaViewSet(MultiSerializerViewSet):
    queryset = Materia.objects.all()
    serializers = {
        'default':    MateriaSerializer,
        'create':  MateriaPostSerializer,
        'retrieve': MateriaPostSerializer,
        'update': MateriaPostSerializer,
    }


    def get_queryset(self):
        queryset = Materia.objects.all()
        plan_id = self.request.query_params.get('planId', None)
        curso_nombre = self.request.query_params.get('cursoNombre', None)

        if curso_nombre is not None:
            queryset = queryset.filter(nombre__contains=curso_nombre)
        if plan_id is not None:
            queryset = queryset.filter(plan_id=plan_id)
        return queryset


class InscripcionViewSet(ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer


class DocenteViewSet(ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer


class CalificacionViewSet(ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer
