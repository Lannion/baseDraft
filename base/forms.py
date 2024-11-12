from django import forms
from .models import Address, Program, User, Student, Instructor, Course, Schedule, Enrollment, Grade, Permission, Role

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'barangay', 'city', 'province']

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['id', 'abbreviation', 'description']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'middle_name', 'suffix', 'email', 'contact_number', 'username', 'password', 'role']
        widgets = {
            'password': forms.PasswordInput(),  # mask password 
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'middle_name', 'suffix', 'year_level', 'section', 'program', 'address', 
                  'old_or_new', 'status', 'birth_date', 'gender', 'contact_number', 'email']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['first_name', 'last_name', 'middle_name', 'suffix', 'email', 'contact_number', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'program', 'title', 'lab_units', 'lec_units', 'total_units', 'year_level', 'semester', 'school_year', 'pre_requisite']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['course_code', 'program', 'instructor', 'from_time', 'to_time', 'category', 'day', 'room']
        widgets = {
            'from_time': forms.TimeInput(attrs={'type': 'time'}),
            'to_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['course_code', 'program', 'student', 'enrollment_date', 'status', 'school_year', 'checked_by', 'released_by']
        widgets = {
            'enrollment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'school_year': forms.DateInput(attrs={'type': 'date'}),
        }

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'course_code', 'program', 'grade', 'instructor', 'remarks']

class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = ['name', 'description']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role', 'description', 'permissions']
        widgets = {
            'permissions': forms.CheckboxSelectMultiple(),  
        }
