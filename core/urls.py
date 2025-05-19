# backend/core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'site-settings', SiteSettingsViewSet)
router.register(r'hero-section', HeroSectionViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'testimonials', TestimonialViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'blog-posts', BlogPostViewSet)
router.register(r'contact-messages', ContactMessageViewSet)
router.register(r'resume', ResumeViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
]
