from django.contrib import admin
from .models import Project, Certificate, Skill, Contact

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_created', 'featured')
    list_filter = ('category', 'featured', 'date_created')
    search_fields = ('title', 'description', 'technologies')
    date_hierarchy = 'date_created'
    list_editable = ('featured',)

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'date')
    list_filter = ('issuer', 'date')
    search_fields = ('name', 'issuer')
    date_hierarchy = 'date'

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level')
    list_filter = ('category', 'level')
    search_fields = ('name',)
    list_editable = ('level',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_sent', 'is_read')
    list_filter = ('is_read', 'date_sent')
    search_fields = ('name', 'email', 'subject', 'message')
    date_hierarchy = 'date_sent'
    readonly_fields = ('name', 'email', 'subject', 'message', 'date_sent')
    list_editable = ('is_read',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Contact, ContactAdmin)

# Настройка заголовков админ-панели
admin.site.site_header = "Портфолио Администрирование"
admin.site.site_title = "Портфолио"
admin.site.index_title = "Добро пожаловать в админ-панель портфолио"