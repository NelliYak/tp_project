from flask import Blueprint, request, jsonify
from .models import film_manager

bp = Blueprint('api', __name__, url_prefix='/api')

# Получить все фильмы
@bp.route('/films', methods=['GET'])
def get_films():
    films = film_manager.get_all_films()
    return jsonify(films)

# Получить один фильм
@bp.route('/films/<int:film_id>', methods=['GET'])
def get_film(film_id):
    films = film_manager.get_all_films()
    for film in films:
        if film['id'] == film_id:
            return jsonify(film)
    return jsonify({'error': 'Фильм не найден'}), 404

# Добавить фильм
@bp.route('/films', methods=['POST'])
def add_film():
    data = request.get_json()
    
    # Проверка обязательных полей
    if not data.get('title') or not data.get('year') or not data.get('genre'):
        return jsonify({'error': 'Необходимы title, year и genre'}), 400
    
    film = film_manager.add_film(data)
    return jsonify(film), 201

# Удалить фильм
@bp.route('/films/<int:film_id>', methods=['DELETE'])
def delete_film(film_id):
    result = film_manager.delete_film(film_id)
    if result:
        return jsonify({'message': 'Фильм удален', 'film': result})
    return jsonify({'error': 'Фильм не найден'}), 404

# Проверка здоровья (уже была)
@bp.route('/health')
def health():
    return jsonify({"status": "ok", "message": "API работает"})
