// Плавная прокрутка для якорных ссылок
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            window.scrollTo({
                top: target.offsetTop - 80,
                behavior: 'smooth'
            });
        }
    });
});

// Анимация прогресс-баров навыков
function animateSkills() {
    const skillBars = document.querySelectorAll('.skill-progress-bar');
    
    skillBars.forEach(bar => {
        const targetWidth = bar.getAttribute('data-width');
        bar.style.width = '0%';
        
        setTimeout(() => {
            bar.style.width = targetWidth + '%';
        }, 500);
    });
}

// Запуск анимации при прокрутке до секции навыков
document.addEventListener('DOMContentLoaded', function() {
    const skillsSection = document.querySelector('#skills');
    if (skillsSection) {
        window.addEventListener('scroll', () => {
            const sectionPos = skillsSection.getBoundingClientRect().top;
            const screenPos = window.innerHeight / 1.3;
            
            if (sectionPos < screenPos) {
                animateSkills();
                // Удаляем обработчик после первого срабатывания
                window.removeEventListener('scroll', arguments.callee);
            }
        });
    }
});

// Кнопка "Наверх"
document.addEventListener('DOMContentLoaded', function() {
    const backToTopButton = document.getElementById('back-to-top');
    
    if (backToTopButton) {
        // Показать/скрыть кнопку при прокрутке
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                backToTopButton.classList.add('show');
            } else {
                backToTopButton.classList.remove('show');
            }
        });
        
        // Прокрутка наверх при клике
        backToTopButton.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
});