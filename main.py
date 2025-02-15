from flask import Flask, json, redirect, render_template, url_for
from flask import request, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return jsonify(error="This path does not exist."), 404

# Загрузка данных из JSON (вместо базы данных)
with open('data/memorials.json', 'r', encoding='utf-8') as f:
    memorials_data = json.load(f)
    
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/map', methods=["GET"])
def map():
    return render_template("map.html")

# Страница администратора
@app.route('/admin')
def admin():
    return render_template('admin.html')

# Страница авторизованного пользователя
@app.route('/user')
def user():
    return render_template('user.html')

# Страница с информацией о погибшем
@app.route('/memorial/<int:memorial_id>')
def memorial(memorial_id):
    memorial = next((m for m in memorials_data if m['id'] == memorial_id), None)
    if memorial:
        return render_template('memorial.html', memorial=memorial)
    return "Запись не найдена", 404

@app.route('/api/memorials')
def api_memorials():
    return jsonify(memorials_data)

app.run("127.0.0.1", 80, debug=True) 