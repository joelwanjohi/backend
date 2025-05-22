# backend/core/views.py
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework import viewsets
import os
import mimetypes
from .models import *
from .serializers import *

def create_admin_user(request):
    if not User.objects.filter(username="joeli").exists():
        User.objects.create_superuser(
            username="joeli",
            email="wabjohijoel207@gmail.com",
            password="12345678"
        )
        return HttpResponse("✅ Superuser 'joeli' created successfully.")
    else:
        return HttpResponse("⚠️ Superuser 'joeli' already exists.")

def home(request):
    return HttpResponse("Welcome to TechwithJoel's Portfolio API. Visit /api/ for endpoints or /admin/ for management.")

def serve_media(request, path):
    """Serve media files in production"""
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    
    if os.path.exists(file_path):
        content_type, _ = mimetypes.guess_type(file_path)
        if content_type is None:
            content_type = 'application/octet-stream'
        
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type=content_type)
            return response
    else:
        raise Http404("File not found")

class SiteSettingsViewSet(viewsets.ModelViewSet):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer

class HeroSectionViewSet(viewsets.ModelViewSet):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all().order_by('order')
    serializer_class = ResumeSerializer