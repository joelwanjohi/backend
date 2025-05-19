# backend/core/models.py
from django.db import models
from ckeditor.fields import RichTextField

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default="Irungu's Portfolio")
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    footer_text = models.CharField(max_length=200, default="© 2025 Irungu")
    resume_file = models.FileField(upload_to='resume/', blank=True)

    def __str__(self):
        return self.site_name

class HeroSection(models.Model):
    headline = models.CharField(max_length=200, default="Irungu – Developer | Innovator | Tech Explorer")
    subheadline = models.CharField(max_length=300, default="Building the future with code and creativity")
    cta_text = models.CharField(max_length=50, default="View Work")
    cta_link = models.CharField(max_length=200, default="#projects")
    secondary_cta_text = models.CharField(max_length=50, default="Contact Me")
    secondary_cta_link = models.CharField(max_length=200, default="#contact")
    background_image = models.ImageField(upload_to='hero/', blank=True)

    def __str__(self):
        return self.headline

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skills/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    tech_stack = models.CharField(max_length=200)
    category = models.CharField(max_length=100, default="Web")
    image = models.ImageField(upload_to='projects/', blank=True)
    demo_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    video_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.company}"

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='services/', null=True, blank=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    tags = models.CharField(max_length=200, blank=True)
    cover_image = models.ImageField(upload_to='blogs/', blank=True)
    live_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Resume(models.Model):
    category = models.CharField(max_length=100, choices=[
        ('education', 'Education'),
        ('experience', 'Work Experience'),
        ('certification', 'Certification'),
    ])
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = RichTextField(blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.organization}"
