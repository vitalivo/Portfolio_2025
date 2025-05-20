document.addEventListener('DOMContentLoaded', function() {
    // Инициализация переключателя темы
    initThemeToggle();
    
    // Инициализация предпросмотра проектов
    initProjectPreview();
    
    // Инициализация фильтров проектов
    initProjectFilters();
    
    // Плавная прокрутка для якорных ссылок
    initSmoothScroll();
});

// Функция для переключения темы
function initThemeToggle() {
    const themeToggleBtn = document.getElementById('theme-toggle-btn');
    const darkIcon = document.querySelector('.dark-icon');
    const lightIcon = document.querySelector('.light-icon');
    
    if (!themeToggleBtn) return;
    
    // Проверяем сохраненную тему
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
        darkIcon.classList.add('d-none');
        lightIcon.classList.remove('d-none');
    }
    
    themeToggleBtn.addEventListener('click', function() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        
        if (currentTheme === 'dark') {
            document.documentElement.removeAttribute('data-theme');
            localStorage.setItem('theme', 'light');
            darkIcon.classList.remove('d-none');
            lightIcon.classList.add('d-none');
        } else {
            document.documentElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
            darkIcon.classList.add('d-none');
            lightIcon.classList.remove('d-none');
        }
    });
}

// Функция для предпросмотра проектов
function initProjectPreview() {
    const previewButtons = document.querySelectorAll('.preview-btn');
    const modal = document.getElementById('projectPreviewModal');
    
    if (!previewButtons.length || !modal) return;
    
    previewButtons.forEach(button => {
        button.addEventListener('click', function() {
            const projectId = this.getAttribute('data-id');
            fetchProjectPreview(projectId);
        });
    });
    
    // Функция для загрузки данных проекта через AJAX
    function fetchProjectPreview(projectId) {
        fetch(`/api/project/${projectId}/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Заполняем модальное окно данными
                document.getElementById('previewTitle').textContent = data.title;
                document.getElementById('previewImage').src = data.image;
                document.getElementById('previewImage').alt = data.title;
                document.getElementById('previewDescription').textContent = data.preview_description;
                document.getElementById('previewCategory').textContent = data.category;
                
                // Заполняем технологии
                const techContainer = document.getElementById('previewTechnologies');
                techContainer.innerHTML = '';
                data.technologies.split(',').forEach(tech => {
                    const span = document.createElement('span');
                    span.className = 'badge bg-primary me-1 mb-1';
                    span.textContent = tech.trim();
                    techContainer.appendChild(span);
                });
                
                // Устанавливаем ссылки
                const demoLink = document.getElementById('previewDemoLink');
                const codeLink = document.getElementById('previewCodeLink');
                const detailLink = document.getElementById('previewDetailLink');
                
                if (data.demo_link) {
                    demoLink.href = data.demo_link;
                    demoLink.style.display = 'inline-block';
                } else {
                    demoLink.style.display = 'none';
                }
                
                if (data.code_link) {
                    codeLink.href = data.code_link;
                    codeLink.style.display = 'inline-block';
                } else {
                    codeLink.style.display = 'none';
                }
                
                detailLink.href = `/project/${data.id}/`;
                
                // Открываем модальное окно
                const previewModal = new bootstrap.Modal(document.getElementById('projectPreviewModal'));
                previewModal.show();
            })
            .catch(error => {
                console.error('Error fetching project data:', error);
                alert('Не удалось загрузить данные проекта. Пожалуйста, попробуйте позже.');
            });
    }
}

// Функция для фильтрации проектов
function initProjectFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectItems = document.querySelectorAll('.project-item');
    
    if (!filterButtons.length || !projectItems.length) return;
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Удаляем активный класс у всех кнопок
            filterButtons.forEach(btn => btn.classList.remove('active'));
            // Добавляем активный класс текущей кнопке
            this.classList.add('active');
            
            const filter = this.getAttribute('data-filter');
            
            projectItems.forEach(item => {
                if (filter === 'all' || item.getAttribute('data-category') === filter) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });
}

// Функция для плавной прокрутки
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Функция для показа всех сертификатов
function showAllCertificates() {
    const hiddenCertificates = document.querySelectorAll('.hidden-certificate');
    const showAllBtn = document.getElementById('showAllCertificatesBtn');
    const showLessBtn = document.getElementById('showLessCertificatesBtn');
    
    if (!hiddenCertificates.length || !showAllBtn || !showLessBtn) return;
    
    hiddenCertificates.forEach(cert => {
        cert.style.display = 'block';
    });
    
    showAllBtn.style.display = 'none';
    showLessBtn.style.display = 'inline-block';
}

// Функция для скрытия сертификатов
function showLessCertificates() {
    const hiddenCertificates = document.querySelectorAll('.hidden-certificate');
    const showAllBtn = document.getElementById('showAllCertificatesBtn');
    const showLessBtn = document.getElementById('showLessCertificatesBtn');
    
    if (!hiddenCertificates.length || !showAllBtn || !showLessBtn) return;
    
    hiddenCertificates.forEach(cert => {
        cert.style.display = 'none';
    });
    
    showAllBtn.style.display = 'inline-block';
    showLessBtn.style.display = 'none';
}