from django.contrib import admin
from .models import Project, Skill, Certificate, Contact

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'featured', 'created_at')
    list_filter = ('featured', 'created_at')
    search_fields = ('title', 'description', 'technologies')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'date')
    search_fields = ('name', 'issuer')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')