from django.shortcuts import render
from .models import Course, Student
# Create your views here.
def courselist(request):
    course = Course.objects.all()
    return render(request, 'course/clist.html', {'cno':course})

def studentlist(request):
    st = Student.objects.all()
    return render(request, 'course/slist.html', {'sno': st})

