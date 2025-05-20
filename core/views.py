from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.contrib import messages
from .models import Project, Certificate, Skill, Contact
from .forms import ContactForm

@cache_page(60 * 15)  # кэширование на 15 минут
def home(request):
    projects = Project.objects.filter(featured=True)[:4]
    certificates = Certificate.objects.all()[:9]
    skills = Skill.objects.all()
    
    # Группировка навыков по категориям
    language_skills = skills.filter(category='language')
    framework_skills = skills.filter(category='framework')
    tool_skills = skills.filter(category='tool')
    
    context = {
        'projects': projects,
        'certificates': certificates,
        'language_skills': language_skills,
        'framework_skills': framework_skills,
        'tool_skills': tool_skills,
    }
    return render(request, 'home.html', context)

def about(request):
    skills = Skill.objects.all()
    return render(request, 'about.html', {'skills': skills})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    # Получаем другие проекты для секции "Похожие проекты"
    related_projects = Project.objects.filter(category=project.category).exclude(pk=pk)[:3]
    return render(request, 'project_detail.html', {
        'project': project,
        'related_projects': related_projects
    })

def certificates(request):
    certificates = Certificate.objects.all()
    return render(request, 'certificates.html', {'certificates': certificates})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def project_preview_api(request, pk):
    try:
        project = Project.objects.get(pk=pk)
        data = {
            'id': project.id,
            'title': project.title,
            'image': project.image.url,
            'thumbnail': project.thumbnail.url if project.thumbnail else project.image.url,
            'preview_description': project.preview_description,
            'technologies': project.technologies,
            'category': project.get_category_display(),
            'demo_link': project.demo_link,
            'code_link': project.code_link,
        }
        return JsonResponse(data)
    except Project.DoesNotExist:
        return JsonResponse({'error': 'Project not found'}, status=404)