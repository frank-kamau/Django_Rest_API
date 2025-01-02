from http import HTTPStatus

from rest_framework.decorators import api_view
from rest_framework.response import Response

from apis.models import Student
from apis.my_serializers import StudentSerializer


# Create your views here.
@api_view(['GET'])
def students_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


def single_student(request):
    return None


def update_student(request):
    return None


def delete_student(request):
    return None

@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTPStatus.CREATED)
    return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)