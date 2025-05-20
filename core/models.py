from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='projects/', verbose_name="Изображение")
    technologies = models.CharField(max_length=255, verbose_name="Технологии")
    demo_link = models.URLField(blank=True, null=True, verbose_name="Ссылка на демо")
    code_link = models.URLField(blank=True, null=True, verbose_name="Ссылка на код")
    featured = models.BooleanField(default=False, verbose_name="Избранный")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('language', 'Язык программирования'),
        ('framework', 'Фреймворк/библиотека'),
        ('tool', 'Инструмент/технология'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Название")
    level = models.IntegerField(default=0, verbose_name="Уровень (0-100)")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Категория")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

class Certificate(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    issuer = models.CharField(max_length=100, verbose_name="Выдан")
    date = models.CharField(max_length=50, verbose_name="Дата")
    image = models.ImageField(upload_to='certificates/', verbose_name="Изображение")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Тема")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"