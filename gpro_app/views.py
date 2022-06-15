from django.shortcuts import render

# Create your views here.
def subjects(request):
    return render(request,'pages/subjects.html')

def classes(request):
    return render(request,'pages/classes.html')

def lecturers(request):
    return render(request,'pages/lecturers.html')

def yearlyStudents(request):
    return render(request,'pages/yearly_students.html')
