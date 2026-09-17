from django.shortcuts import render, redirect
from .models import Student


def home(request):
    return render(request, 'students/home.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            student_id=request.POST['student_id'],
            name=request.POST['name'],
            department=request.POST['department'],
            year=request.POST['year'],
            email=request.POST['email'],
            phone=request.POST['phone']
        )

        return redirect('student_list')

    return render(request, 'students/add_student.html')


def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.student_id = request.POST['student_id']
        student.name = request.POST['name']
        student.department = request.POST['department']
        student.year = request.POST['year']
        student.email = request.POST['email']
        student.phone = request.POST['phone']

        student.save()

        return redirect('student_list')

    return render(request, 'students/edit_student.html', {'student': student})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()

    return redirect('student_list')