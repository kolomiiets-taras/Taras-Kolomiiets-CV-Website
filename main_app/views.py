from django.shortcuts import render
from .models import *


def main_page(request):
    profile = Profile.objects.get(first_name='Taras')
    education = Education.objects.filter(profile=profile)
    languages = Language.objects.filter(profile=profile)
    skills = TechSkill.objects.filter(profile=profile).order_by('-level')
    projects = Project.objects.filter(profile=profile)
    resume = Resume.objects.filter(profile=profile).first()

    context = {'profile': profile,
               'education': education,
               'languages': languages,
               'skills': skills,
               'projects': projects,
               'resume': resume
               }
    return render(request, 'index.html', context)
