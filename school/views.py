from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from school.models import Student, Course, Register
from school.serializing import StudentSerializer, CourseSerializer, RegisterSerializer, ListRegisterStudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """ Show the students """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    """ Show the courses """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    """ Show the registers """
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer


class ListRegisterStudent(generics.ListAPIView):
    """ Show the Registers in Courses from Student """

    def get_queryset(self):
        queryset = Register.objects.filter(student_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListRegisterStudentSerializer
