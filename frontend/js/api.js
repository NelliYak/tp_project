// Конфигурация API
const API_BASE_URL = 'http://localhost:5000/api';

// Все функции для работы с API
const api = {
    // Получить все фильмы
    async getFilms() {
        try {
            const response = await fetch(`${API_BASE_URL}/films`);
            return await response.json();
        } catch (error) {
            console.error('Ошибка при загрузке фильмов:', error);
            return [];
        }
    },

    // Добавить фильм
    async addFilm(filmData) {
        try {
            const response = await fetch(`${API_BASE_URL}/films`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(filmData)
            });
            return await response.json();
        } catch (error) {
            console.error('Ошибка при добавлении фильма:', error);
            return null;
        }
    },

    // Удалить фильм
    async deleteFilm(id) {
        try {
            const response = await fetch(`${API_BASE_URL}/films/${id}`, {
                method: 'DELETE'
            });
            return await response.json();
        } catch (error) {
            console.error('Ошибка при удалении фильма:', error);
            return null;
        }
    },

    // Поиск фильмов (пока просто фильтрация на клиенте)
    async searchFilms(query) {
        const films = await this.getFilms();
        if (!query) return films;
        
        const searchLower = query.toLowerCase();
        return films.filter(film => 
            film.title.toLowerCase().includes(searchLower) ||
            film.genre.toLowerCase().includes(searchLower)
        );
    }
};

// Экспорт для использования в других файлах
if (typeof module !== 'undefined' && module.exports) {
    module.exports = api;
}
