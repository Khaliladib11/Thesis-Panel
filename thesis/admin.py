from django.contrib import admin
from .models import Person, Student, Supervisor, Course, Field, Thesis

# Register your models here.
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Supervisor)
admin.site.register(Course)
admin.site.register(Field)
admin.site.register(Thesis)