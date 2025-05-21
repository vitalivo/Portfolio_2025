from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview_description = models.TextField(blank=True, null=True, verbose_name="Краткое описание для предпросмотра")
    technologies = models.CharField(max_length=200, verbose_name="Технологии")
    image = ProcessedImageField(
        upload_to='projects/',
        processors=[ResizeToFill(1200, 800)],
        format='JPEG',
        options={'quality': 85},
        verbose_name="Изображение проекта"
    )
    thumbnail = ProcessedImageField(
        upload_to='projects/thumbnails/',
        processors=[ResizeToFill(400, 300)],
        format='JPEG',
        options={'quality': 80},
        verbose_name="Миниатюра",
        blank=True,
        null=True
    )
    demo_link = models.URLField(blank=True, null=True, verbose_name="Ссылка на демо")
    code_link = models.URLField(blank=True, null=True, verbose_name="Ссылка на код")
    preview_url = models.URLField(
        blank=True, 
        verbose_name="URL для предпросмотра",
        help_text="URL для встроенного предпросмотра проекта (например, GitHub Pages)"
    )
    featured = models.BooleanField(default=False, verbose_name="Избранный")
    category = models.CharField(max_length=50, choices=[
        ('web', 'Веб-разработка'),
        ('mobile', 'Мобильные приложения'),
        ('desktop', 'Десктопные приложения'),
        ('other', 'Другое')
    ], default='web', verbose_name="Категория")
    date_created = models.DateField(verbose_name="Дата создания")
    
    # SEO поля
    meta_title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Meta Title")
    meta_description = models.TextField(blank=True, null=True, verbose_name="Meta Description")
    meta_keywords = models.CharField(max_length=255, blank=True, null=True, verbose_name="Meta Keywords")
    
    def save(self, *args, **kwargs):
        # Если краткое описание не заполнено, создаем его из основного
        if not self.preview_description:
            if len(self.description) > 150:
                self.preview_description = self.description[:150] + "..."
            else:
                self.preview_description = self.description
                
        # Если мета-заголовок не заполнен, используем название проекта
        if not self.meta_title:
            self.meta_title = self.title
            
        # Если мета-описание не заполнено, используем краткое описание
        if not self.meta_description:
            self.meta_description = self.preview_description
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ['-date_created']


class Certificate(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    issuer = models.CharField(max_length=200, verbose_name="Выдан")
    date = models.DateField(verbose_name="Дата получения")
    image = models.ImageField(upload_to='certificates/', verbose_name="Изображение")
    url = models.URLField(blank=True, null=True, verbose_name="Ссылка на сертификат")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"
        ordering = ['-date']


class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    level = models.IntegerField(default=80, verbose_name="Уровень (0-100)")
    category = models.CharField(max_length=50, choices=[
        ('language', 'Языки программирования'),
        ('framework', 'Фреймворки и библиотеки'),
        ('tool', 'Инструменты и технологии')
    ], default='language', verbose_name="Категория")
    color = models.CharField(max_length=50, default="from-blue-500 to-blue-700", verbose_name="Цвет градиента")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
        ordering = ['-level']


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Тема")
    message = models.TextField(verbose_name="Сообщение")
    date_sent = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ['-date_sent']