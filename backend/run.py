from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/health')
def health():
    return jsonify({"status": "ok", "message": "API работает"})

if __name__ == '__main__':
    print("🚀 Сервер запущен: http://localhost:5000")
    app.run(debug=True, port=5000)
