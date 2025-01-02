from rest_framework.decorators import api_view

from apis.models import Student


# Create your views here.
@api_view(['GET'])
def students_list(request):
    students = Student.objects.all()
    return None


def single_student(request):
    return None


def update_student(request):
    return None


def delete_student(request):
    return None


def create_student(request):
    return None