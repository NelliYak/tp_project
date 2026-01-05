from flask import Blueprint, request, jsonify
from .models import film_manager

bp = Blueprint('api', __name__, url_prefix='/api')


# 1. Проверка здоровья
@bp.route('/health')
def health():
    return jsonify({"status": "ok", "message": "API работает"})


# 2. Получить все фильмы
@bp.route('/films', methods=['GET'])
def get_films():
    films = film_manager.get_all_films()
    return jsonify(films)


# 3. Получить один фильм
@bp.route('/films/<int:film_id>', methods=['GET'])
def get_film(film_id):
    films = film_manager.get_all_films()
    for film in films:
        if film['id'] == film_id:
            return jsonify(film)
    return jsonify({'error': 'Фильм не найден'}), 404


# 4. Добавить фильм
@bp.route('/films', methods=['POST'])
def add_film():
    data = request.get_json()

    if not data or not data.get('title') or not data.get('year') or not data.get('genre'):
        return jsonify({'error': 'Необходимы title, year и genre'}), 400

    film = film_manager.add_film(data)
    return jsonify(film), 201


# 5. ОБНОВИТЬ ФИЛЬМ (НОВАЯ ФУНКЦИЯ)
@bp.route('/films/<int:film_id>', methods=['PUT'])
def update_film(film_id):
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Нет данных для обновления'}), 400

    film = film_manager.update_film(film_id, data)

    if film:
        return jsonify({
            'message': 'Фильм успешно обновлен',
            'film': film
        })

    return jsonify({'error': 'Фильм не найден'}), 404


# 6. Удалить фильм
@bp.route('/films/<int:film_id>', methods=['DELETE'])
def delete_film(film_id):
    film = film_manager.delete_film(film_id)
    if film:
        return jsonify({'message': 'Фильм удален', 'film': film})
    return jsonify({'error': 'Фильм не найден'}), 404