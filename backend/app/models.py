import json
import os

class FilmManager:
    def __init__(self, data_file='../data/films.json'):
        self.data_file = os.path.join(os.path.dirname(__file__), data_file)
    
    def get_all_films(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def save_films(self, films):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(films, f, ensure_ascii=False, indent=2)
    
    def add_film(self, film_data):
        films = self.get_all_films()
        new_id = max([f['id'] for f in films], default=0) + 1
        film_data['id'] = new_id
        films.append(film_data)
        self.save_films(films)
        return film_data
    
    def delete_film(self, film_id):
        films = self.get_all_films()
        for i, film in enumerate(films):
            if film['id'] == film_id:
                deleted_film = films.pop(i)
                self.save_films(films)
                return deleted_film
        return None

    def update_film(self, film_id, film_data):
        """Обновить фильм по ID"""
        films = self.get_all_films()
        
        for i, film in enumerate(films):
            if film["id"] == film_id:
                # Обновляем только переданные поля
                for key, value in film_data.items():
                    if key != "id":  # Не позволяем менять ID
                        films[i][key] = value
                
                self.save_films(films)
                return films[i]
        
        return None
        films = self.get_all_films()
        for i, film in enumerate(films):
            if film['id'] == film_id:
                deleted_film = films.pop(i)
                self.save_films(films)
                return deleted_film
        return None

    def toggle_favorite(self, film_id):
        """Добавить/удалить из избранного"""
        films = self.get_all_films()

        for film in films:
            if film['id'] == film_id:
                # Если поле favorite есть - переключаем, иначе ставим true
                film['favorite'] = not film.get('favorite', False)
                self.save_films(films)
                return film

        return None

    def get_favorites(self):
        """Получить все избранные фильмы"""
        films = self.get_all_films()
        return [film for film in films if film.get('favorite', False)]


film_manager = FilmManager()
