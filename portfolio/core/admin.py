from django.contrib import admin
from .models import About, Education, Experience, Portfolio

# Register your models here.
admin.site.register(About)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Portfolio)