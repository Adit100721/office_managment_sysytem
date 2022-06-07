from django.contrib import admin
from .models import Empolyee,role,Department

admin.site.register(Department)
admin.site.register(role)
admin.site.register(Empolyee)

