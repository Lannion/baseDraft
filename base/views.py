from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm 
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Address, Program, User, Student, Instructor, Course, Schedule, Enrollment, Grade, Permission, Role
from .forms import AddressForm, ProgramForm, UserForm, StudentForm, InstructorForm, CourseForm, ScheduleForm, EnrollmentForm, GradeForm


def home(request):
	return render(request, 'base/home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a homepage or dashboard
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form}) #directory sa html containing credentials also passing the class model


# Address Views
class AddressListView(ListView):
    model = Address
    template_name = 'address_list.html'# name ng file

class AddressDetailView(DetailView):
    model = Address
    template_name = 'address_detail.html'

class AddressCreateView(CreateView):
    model = Address
    form_class = AddressForm
    template_name = 'address_form.html'
    success_url = reverse_lazy('address_list')

class AddressUpdateView(UpdateView):
    model = Address
    form_class = AddressForm
    template_name = 'address_form.html'
    success_url = reverse_lazy('address_list')

class AddressDeleteView(DeleteView):
    model = Address
    template_name = 'address_confirm_delete.html'
    success_url = reverse_lazy('address_list')


class ProgramListView(ListView):
    model = Program
    template_name = 'program_list.html'

class ProgramDetailView(DetailView):
    model = Program
    template_name = 'program_detail.html'

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program_list')

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program_list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_confirm_delete.html'
    success_url = reverse_lazy('program_list')


class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
