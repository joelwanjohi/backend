# backend/core/admin.py
from django.contrib import admin
from .models import (
    SiteSettings, HeroSection, Skill, Project,
    Testimonial, Service, BlogPost, ContactMessage, Resume
)

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'github_url', 'linkedin_url', 'resume_file')

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('headline', 'subheadline')

@admin.register(Skill)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'demo_link', 'github_link', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'tech_stack')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'live_link', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'tags')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'short_message', 'created_at')
    list_display_links = ('name', 'short_message')
    search_fields = ('name', 'email', 'message')
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email')
        }),
        ('Message', {
            'fields': ('message',),
            'classes': ('wide',)
        }),
        ('System Information', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at',)
    
    def short_message(self, obj):
        # Return the first 50 characters of the message
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    
    short_message.short_description = 'Message'  # Column header in admin

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'organization', 'start_date', 'end_date')
    list_filter = ('category',)
    search_fields = ('title', 'organization')
