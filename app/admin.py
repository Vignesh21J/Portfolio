from django.contrib import admin
from .models import Home, About, Skills, Profile, Category, Portfolio, ContactFormLog

# Register your models here.
admin.site.register(Home)

class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 3

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]


class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 3

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]
    
admin.site.register(Portfolio)

@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):
    
    list_display = [
        'email',
        'is_success',
        'is_error',
        'action_time',
    ]

    def has_add_permission(self, request, object = None):
        return False
    
    # Show to disable update permission
    def has_change_permission(self, request, object = None):
        return False
    
    #Show to disable delete permission
    def has_delete_permission(self, request, object = None):
        return False