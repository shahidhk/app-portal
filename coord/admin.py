from django.contrib import admin
from coord.models import *

class AnswerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Answer, AnswerAdmin)

class CredentialsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Credentials, CredentialsAdmin)

class ReferenceAdmin(admin.ModelAdmin):
    pass
admin.site.register(References, ReferenceAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Application, ApplicationAdmin)

