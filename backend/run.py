from app import create_app

app = create_app()

if __name__ == '__main__':
    print("🚀 Сервер запущен на http://localhost:5000")
    print("📚 API доступно:")
    print("   GET  /api/health        - проверка работы")
    print("   GET  /api/films         - все фильмы")
    print("   GET  /api/films/<id>    - один фильм")
    print("   POST /api/films         - добавить фильм")
    print("   DELETE /api/films/<id>  - удалить фильм")
    app.run(debug=True, port=5000)
