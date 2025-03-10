from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Teacher
from .forms import StudentForm, TeacherForm  # Create forms (see below)

def index(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'school/index.html', {'students': students, 'teachers': teachers})

# Student CRUD operations

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index page
    else:
        form = StudentForm()
    return render(request, 'school/student_form.html', {'form': form, 'action': 'Create'})

def student_read(request, pk):  # pk = primary key
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'school/student_detail.html', {'student': student})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student) # instance for update
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm(instance=student)
    return render(request, 'school/student_form.html', {'form': form, 'action': 'Update'})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('index')
    return render(request, 'school/student_confirm_delete.html', {'student': student})


def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TeacherForm()
    return render(request, 'school/teacher_form.html', {'form': form, 'action': 'Create'})

def teacher_read(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'school/teacher_detail.html', {'teacher': teacher})

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'school/teacher_form.html', {'form': form, 'action': 'Update'})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('index')
    return render(request, 'school/teacher_confirm_delete.html', {'teacher': teacher})
