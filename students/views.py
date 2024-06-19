#from rest_framework import viewsets
#from .models import Student
#from .serializers import StudentSerializer

#class StudentViewSet(viewsets.ModelViewSet):
#    queryset = Student.objects.all()
#    serializer_class = StudentSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'email']
    search_fields = ['name', 'email']
    ordering_fields = ['name', 'enrollment_date']
