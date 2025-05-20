from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, Certificate
from .forms import ContactForm

def home(request):
    # Получаем данные из моделей
    projects = Project.objects.all()[:4]  # Только избранные проекты для главной страницы
    
    programming_languages = Skill.objects.filter(category='language')
    frameworks = Skill.objects.filter(category='framework')
    tools = Skill.objects.filter(category='tool')
    
    certificates = Certificate.objects.all()[:6]  # Только 6 сертификатов для главной страницы
    
    # Обработка контактной формы
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено!')
            return redirect('home')
    else:
        form = ContactForm()
    
    context = {
        'projects': projects,
        'programming_languages': programming_languages,
        'frameworks': frameworks,
        'tools': tools,
        'certificates': certificates,
        'form': form,
    }
    
    return render(request, 'home.html', context)

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def certificates(request):
    certificates = Certificate.objects.all()
    return render(request, 'certificates.html', {'certificates': certificates})