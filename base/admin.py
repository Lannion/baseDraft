from django.contrib import admin
from .models import Address, Program, User, Student, Instructor, Course, Schedule, Enrollment, Grade, Permission, Role, RolePermission

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'barangay', 'city', 'province')
    search_fields = ('city', 'province')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'abbreviation', 'description')
    search_fields = ('id', 'abbreviation')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'role')
    search_fields = ('username', 'email')
    list_filter = ('role',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'year_level', 'section', 'program', 'status')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('year_level', 'status', 'program', 'gender')

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_number')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('email',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'program', 'year_level', 'semester')
    search_fields = ('code', 'title')
    list_filter = ('program', 'year_level', 'semester')

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'program', 'instructor', 'day', 'from_time', 'to_time', 'category', 'room')
    search_fields = ('course_code', 'room')
    list_filter = ('program', 'instructor', 'day', 'category')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course_code', 'program', 'enrollment_date', 'status', 'school_year')
    search_fields = ('course_code', 'student__first_name', 'student__last_name')
    list_filter = ('status', 'school_year', 'program')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course_code', 'program', 'grade', 'instructor', 'remarks')
    search_fields = ('course_code', 'student__first_name', 'student__last_name')
    list_filter = ('remarks',)

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role', 'description')
    search_fields = ('role',)
    filter_horizontal = ('permissions',)

@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ('role', 'permission')
    list_filter = ('role', 'permission')
