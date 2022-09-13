from django.contrib import admin
from .models import *


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectImageInline,
    ]


admin.site.register(Project, ProjectAdmin)

admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(TechSkill)
admin.site.register(Language)
admin.site.register(Resume)



