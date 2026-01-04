// Главный файл приложения

// Загрузить и отобразить фильмы
async function loadFilms() {
    const films = await api.getFilms();
    displayFilms(films);
}

// Отобразить фильмы в интерфейсе
function displayFilms(films) {
    const container = document.getElementById('filmsList');
    const countElement = document.getElementById('filmCount');
    
    countElement.textContent = films.length;
    
    if (films.length === 0) {
        container.innerHTML = '<p class="no-films">Фильмы не найдены</p>';
        return;
    }
    
    let html = '';
    
    films.forEach(film => {
        html += `
            <div class="film-card" data-id="${film.id}">
                <div class="film-header">
                    <div class="film-title">${film.title}</div>
                    <div class="film-year">${film.year}</div>
                </div>
                
                <div class="film-genre">${film.genre}</div>
                
                ${film.rating ? `
                    <div class="film-rating">⭐ ${film.rating}/10</div>
                ` : ''}
                
                ${film.description ? `
                    <div class="film-description">${film.description}</div>
                ` : ''}
                
                <div class="film-actions">
                    <button class="delete-btn" onclick="deleteFilm(${film.id})">
                        🗑️ Удалить
                    </button>
                </div>
            </div>
        `;
    });
    
    container.innerHTML = html;
}

// Добавить фильм
async function addFilm() {
    const title = document.getElementById('titleInput').value.trim();
    const year = document.getElementById('yearInput').value;
    const genre = document.getElementById('genreInput').value.trim();
    
    if (!title || !year || !genre) {
        alert('Заполните все обязательные поля');
        return;
    }
    
    const filmData = {
        title,
        year: parseInt(year),
        genre,
        rating: 0,
        description: '',
        favorite: false
    };
    
    const result = await api.addFilm(filmData);
    
    if (result) {
        // Очищаем форму
        document.getElementById('titleInput').value = '';
        document.getElementById('yearInput').value = '';
        document.getElementById('genreInput').value = '';
        
        // Обновляем список
        await loadFilms();
        alert('Фильм успешно добавлен!');
    } else {
        alert('Ошибка при добавлении фильма');
    }
}

// Удалить фильм
async function deleteFilm(id) {
    if (!confirm('Вы уверены, что хотите удалить этот фильм?')) {
        return;
    }
    
    const result = await api.deleteFilm(id);
    
    if (result) {
        await loadFilms();
        alert('Фильм удален');
    } else {
        alert('Ошибка при удалении фильма');
    }
}

// Поиск фильмов
async function searchFilms() {
    const query = document.getElementById('searchInput').value;
    const films = await api.searchFilms(query);
    displayFilms(films);
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    // Назначаем обработчики событий
    document.getElementById('searchInput').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') searchFilms();
    });
    
    // Загружаем фильмы при старте
    loadFilms();
});
