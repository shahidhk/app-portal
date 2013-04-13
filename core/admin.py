from django.contrib import admin
from core.models import *

class SubDeptAdmin(admin.ModelAdmin):
    pass
admin.site.register(SubDept, SubDeptAdmin)

class QuestionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Question, QuestionAdmin)

