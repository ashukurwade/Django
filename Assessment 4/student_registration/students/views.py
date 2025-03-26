from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from .models import Student

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'students/register.html', {'form': form})

def student_list(request):
    students = Student.objects.all().order_by('-registration_date')
    return render(request, 'students/list.html', {'students': students})