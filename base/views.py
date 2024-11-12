from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Address, Program, User, Student, Instructor, Course, Schedule, Enrollment, Grade, Permission, Role
from .forms import AddressForm, ProgramForm, UserForm, StudentForm, InstructorForm, CourseForm, ScheduleForm, EnrollmentForm, GradeForm

def home(request):
	return render(request, 'base/home.html')

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
