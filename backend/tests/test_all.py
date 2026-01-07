#!/usr/bin/env python
import requests

BASE_URL = "http://localhost:5000/api"

def test_health():
    """Тест проверки здоровья"""
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'ok'
    print("✅ Health check passed")

def test_crud_operations():
    """Тест CRUD операций"""
    # 1. Получить все фильмы
    response = requests.get(f"{BASE_URL}/films")
    assert response.status_code == 200
    films = response.json()
    print(f"✅ Получено фильмов: {len(films)}")
    
    if films:
        first_film = films[0]
        film_id = first_film['id']
        
        # 2. Обновить фильм
        update_data = {"title": f"{first_film['title']} [TEST]"}
        response = requests.put(f"{BASE_URL}/films/{film_id}", json=update_data)
        assert response.status_code == 200
        print("✅ Film update passed")
        
        # 3. Вернуть обратно
        requests.put(f"{BASE_URL}/films/{film_id}", json={"title": first_film['title']})

def test_favorites():
    """Тест избранного"""
    response = requests.get(f"{BASE_URL}/films")
    films = response.json()
    
    if films:
        film_id = films[0]['id']
        
        # 1. Добавить в избранное
        response = requests.post(f"{BASE_URL}/films/{film_id}/favorite")
        assert response.status_code == 200
        print("✅ Add to favorites passed")
        
        # 2. Проверить избранные
        response = requests.get(f"{BASE_URL}/favorites")
        assert response.status_code == 200
        favorites = response.json()
        print(f"✅ Favorites count: {len(favorites)}")
        
        # 3. Убрать из избранного
        response = requests.post(f"{BASE_URL}/films/{film_id}/favorite")
        assert response.status_code == 200
        print("✅ Remove from favorites passed")

def test_search():
    """Тест поиска"""
    # Простой поиск
    response = requests.get(f"{BASE_URL}/films/search?q=интер")
    assert response.status_code == 200
    results = response.json()
    print(f"✅ Search results: {len(results)}")
    
    # Поиск по жанру
    response = requests.get(f"{BASE_URL}/films/search?genre=фантастика")
    assert response.status_code == 200
    print("✅ Genre search passed")

if __name__ == "__main__":
    print("🧪 Начинаю тестирование API...")
    
    try:
        test_health()
        test_crud_operations()
        test_favorites()
        test_search()
        print("\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
    except Exception as e:
        print(f"\n❌ Ошибка тестирования: {e}")
        print("Убедитесь что сервер запущен: python run.py")
