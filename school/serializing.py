import self as self
from rest_framework import serializers
from school.models import Student, Course, Register


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'doc', 'born_date']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'  # you can put all for get all elements defined in class


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        exclude = []  # if it's empty you recover all elements


class ListRegisterStudentSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model =  Register
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()