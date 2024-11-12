from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=55)
    barangay = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    province = models.CharField(max_length=55)

class Program(models.Model):
    id = models.CharField(max_length=55, primary_key=True)
    abbreviation = models.CharField(max_length=55)
    description = models.CharField(max_length=255)

class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55, blank=True, null=True)
    suffix = models.CharField(max_length=55, blank=True, null=True)
    email = models.EmailField(max_length=55)
    contact_number = models.CharField(max_length=55)
    username = models.CharField(max_length=55, unique=True)
    password = models.CharField(max_length=55)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

class Student(models.Model):
    OLD = 'Old'
    NEW = 'New'
    OLD_OR_NEW_CHOICES = [(OLD, 'Old'), (NEW, 'New')]

    REGULAR = 'Regular'
    IRREGULAR = 'Irregular'
    TRANSFEREE = 'Transferee'
    RETURNEE = 'Returnee'
    NEW_STUDENT = 'New_Student'
    STATUS_CHOICES = [
        (REGULAR, 'Regular'), 
        (IRREGULAR, 'Irregular'), 
        (TRANSFEREE, 'Transferee'), 
        (RETURNEE, 'Returnee'), 
        (NEW_STUDENT, 'New Student')
    ]

    MALE = 'Male'
    FEMALE = 'Female'
    PREFER_NOT_TO_SAY = 'Prefer_not_to_say'
    GENDER_CHOICES = [
        (MALE, 'Male'), 
        (FEMALE, 'Female'), 
        (PREFER_NOT_TO_SAY, 'Prefer not to say')
    ]

    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55, blank=True, null=True)
    suffix = models.CharField(max_length=55, blank=True, null=True)
    year_level = models.IntegerField()
    section = models.IntegerField()
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    old_or_new = models.CharField(max_length=3, choices=OLD_OR_NEW_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    birth_date = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=55)
    email = models.EmailField(max_length=55)

class Instructor(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55, blank=True, null=True)
    suffix = models.CharField(max_length=55, blank=True, null=True)
    email = models.EmailField(max_length=55)
    contact_number = models.CharField(max_length=55)
    password = models.CharField(max_length=55)

class Course(models.Model):
    code = models.CharField(max_length=55, primary_key=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    lab_units = models.IntegerField()
    lec_units = models.IntegerField()
    total_units = models.IntegerField()
    year_level = models.IntegerField()
    semester = models.IntegerField()
    school_year = models.CharField(max_length=55)
    pre_requisite = models.CharField(max_length=55, blank=True, null=True)

class Schedule(models.Model):
    LAB = 'lab'
    LEC = 'lec'
    CATEGORY_CHOICES = [(LAB, 'Lab'), (LEC, 'Lec')]

    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    DAY_CHOICES = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday')
    ]

    course_code = models.CharField(max_length=55)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    from_time = models.TimeField()
    to_time = models.TimeField()
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    day = models.CharField(max_length=9, choices=DAY_CHOICES)
    room = models.CharField(max_length=55)

class Enrollment(models.Model):
    ENROLLED = 'enrolled'
    WAITLISTED = 'waitlisted'
    STATUS_CHOICES = [(ENROLLED, 'Enrolled'), (WAITLISTED, 'Waitlisted')]

    course_code = models.CharField(max_length=55)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    school_year = models.DateField()
    checked_by = models.IntegerField()
    released_by = models.IntegerField()

class Grade(models.Model):
    PASSED = 'Passed'
    FAILED = 'Failed'
    INCOMPLETE = 'Incomplete'
    UNCONDITIONAL_FAILURE = 'Unconditional Failure'
    NOT_GRADED_YET = 'Not Graded Yet'
    REMARKS_CHOICES = [
        (PASSED, 'Passed'), 
        (FAILED, 'Failed'), 
        (INCOMPLETE, 'Incomplete'), 
        (UNCONDITIONAL_FAILURE, 'Unconditional Failure'), 
        (NOT_GRADED_YET, 'Not Graded Yet')
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=55)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=20, choices=REMARKS_CHOICES)

class Permission(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()

class Role(models.Model):
    role = models.CharField(max_length=55)
    description = models.TextField()
    permissions = models.ManyToManyField(Permission, through='RolePermission')

class RolePermission(models.Model):
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
