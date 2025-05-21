/**
 * Функция для инициализации предпросмотра проектов с iframe
 * Показывает живую демонстрацию проекта в iframe
 */
function initProjectPreviewIframe() {
  // Находим все кнопки предпросмотра на странице
  const previewButtons = document.querySelectorAll(".preview-btn")

  // Элементы модального окна
  const modal = document.getElementById("projectPreviewModal")
  const previewFrame = document.getElementById("previewFrame")
  const previewContainer = document.getElementById("previewContainer")
  const previewLoading = document.getElementById("previewLoading")
  const previewError = document.getElementById("previewError")
  const previewTitle = document.getElementById("previewTitle")
  const previewTechnologies = document.getElementById("previewTechnologies")
  const previewCodeLink = document.getElementById("previewCodeLink")
  const openInNewTab = document.getElementById("openInNewTab")
  const screenSizeButtons = document.querySelectorAll(".screen-size-btn")

  // Обработчик события для кнопок размера экрана
  screenSizeButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Удаляем активный класс у всех кнопок
      screenSizeButtons.forEach((btn) => btn.classList.remove("active"))

      // Добавляем активный класс текущей кнопке
      this.classList.add("active")

      // Получаем размер экрана из атрибута data-size
      const size = this.getAttribute("data-size")

      // Удаляем все классы размеров у контейнера
      previewContainer.classList.remove("preview-desktop", "preview-tablet", "preview-mobile")

      // Добавляем соответствующий класс
      previewContainer.classList.add(`preview-${size}`)
    })
  })

  // Добавляем обработчик события для каждой кнопки предпросмотра
  previewButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Получаем данные проекта
      const projectId = this.getAttribute("data-id")
      const projectDataElement = document.getElementById(`project-data-${projectId}`)

      if (!projectDataElement) {
        console.error(`Элемент с данными проекта #${projectId} не найден`)
        return
      }

      // Получаем URL для предпросмотра
      const previewUrl = projectDataElement.getAttribute("data-preview-url")
      const title = projectDataElement.getAttribute("data-title")
      const technologies = projectDataElement.getAttribute("data-technologies")
      const codeLink = projectDataElement.getAttribute("data-code-link")

      // Проверяем, есть ли URL для предпросмотра
      if (!previewUrl) {
        previewError.textContent = "URL для предпросмотра не указан"
        previewError.style.display = "block"
        previewLoading.style.display = "none"
        return
      }

      // Заполняем информацию о проекте
      previewTitle.textContent = title
      previewTechnologies.textContent = technologies

      // Обновляем ссылки
      if (codeLink) {
        previewCodeLink.href = codeLink
        previewCodeLink.style.display = "inline-block"
      } else {
        previewCodeLink.style.display = "none"
      }

      openInNewTab.href = previewUrl

      // Сбрасываем состояние модального окна
      previewError.style.display = "none"
      previewLoading.style.display = "flex"
      previewFrame.src = "about:blank"

      // Устанавливаем размер по умолчанию (desktop)
      previewContainer.classList.remove("preview-tablet", "preview-mobile")
      previewContainer.classList.add("preview-desktop")
      screenSizeButtons.forEach((btn) => btn.classList.remove("active"))
      document.querySelector('.screen-size-btn[data-size="desktop"]').classList.add("active")

      // Открываем модальное окно
      const bsModal = new window.bootstrap.Modal(modal)
      bsModal.show()

      // Загружаем iframe после открытия модального окна
      modal.addEventListener(
        "shown.bs.modal",
        function loadIframe() {
          // Удаляем обработчик, чтобы он не вызывался повторно
          modal.removeEventListener("shown.bs.modal", loadIframe)

          // Загружаем URL в iframe
          previewFrame.src = previewUrl

          // Обработчик загрузки iframe
          previewFrame.onload = () => {
            previewLoading.style.display = "none"
          }

          // Обработчик ошибки загрузки iframe
          previewFrame.onerror = () => {
            previewError.textContent = "Не удалось загрузить предпросмотр"
            previewError.style.display = "block"
            previewLoading.style.display = "none"
          }
        },
        { once: true },
      )
    })
  })
}

// Инициализация при загрузке страницы
document.addEventListener("DOMContentLoaded", initProjectPreviewIframe)
