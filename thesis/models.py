from django.db import models
import uuid


# Person Model
class Person(models.Model):
    pid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True, blank=False)
    password = models.CharField(max_length=200, blank=False)
    image_profile = models.ImageField(null=True, blank=True, default='default.jpg')
    linkedIn_link = models.CharField(max_length=250, null=True, blank=True)
    github_link = models.CharField(max_length=250, null=True, blank=True)
    portfolio = models.CharField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name


# Student Model, inherited from Person Model
class Student(models.Model):
    stid = models.OneToOneField(Person, primary_key=True, unique=True, on_delete=models.CASCADE)
    cis = models.ForeignKey('Course', on_delete=models.DO_NOTHING)


# Supervisor Model, inherited from Person Model
class Supervisor(models.Model):
    suid = models.OneToOneField(Person, primary_key=True, unique=True, on_delete=models.CASCADE)
    fields = models.ManyToManyField('Field', blank=False)


# Course available
class Course(models.Model):
    COURSES = (
        ('AI', 'Artificial Intelligence'),
        ('GT', 'Computer Games Technology'),
        ('CS', 'Cyber Security '),
        ('DS', 'Data Science'),
        ('CC', 'Software Engineering with Cloud Computing'),
        ('HC', 'Human-Computer Interaction Design'),
    )
    cid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    course_name = models.CharField(max_length=200, choices=COURSES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.course_name


# Fields Model
class Field(models.Model):
    fid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    field_title = models.CharField(max_length=200, null=False, blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.field_title


class Thesis(models.Model):
    tid = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    stid = models.OneToOneField('Student', unique=True, null=False, blank=False, on_delete=models.DO_NOTHING)
    suid = models.ForeignKey('Supervisor', null=False, blank=False, on_delete=models.DO_NOTHING)
    fid = models.ForeignKey('Field', null=False, blank=False, on_delete=models.DO_NOTHING)

    title = models.CharField(max_length=300, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
