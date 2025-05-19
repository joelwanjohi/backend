# backend/core/serializers.py
from rest_framework import serializers
from .models import *

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = '__all__'

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'
class SkillSerializer(serializers.ModelSerializer):
    icon = serializers.ImageField(max_length=None, use_url=True, allow_null=True)

    class Meta:
        model = Skill
        fields = ['id', 'name', 'icon']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    icon = serializers.ImageField(max_length=None, use_url=True, allow_null=True)

    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'icon']

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'
