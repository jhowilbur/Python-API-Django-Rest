from rest_framework import viewsets
from school.models import Student, Course
from school.serializing import StudentSerializer, CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """ Show the students """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """ Show the students """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
