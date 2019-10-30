from django.contrib import admin
from .models import Freelancer, Skill, Portfolio

# Register your models here.
admin.site.register(Freelancer)
admin.site.register(Skill)
admin.site.register(Portfolio)
