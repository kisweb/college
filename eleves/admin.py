from django.contrib import admin
from .models import Affectation, Classeroom, Agent, Student, Inscription, Absence

# Register your models here.

admin.site.register(Affectation)
admin.site.register(Classeroom)
admin.site.register(Agent)
admin.site.register(Student)
admin.site.register(Inscription)
admin.site.register(Absence)