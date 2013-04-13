from django.contrib import admin
from account.models import *

class AnnouncementAdmin(admin.ModelAdmin):
    pass
admin.site.register(Announcement, AnnouncementAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile, UserProfileAdmin)
