import os
import json
import datetime
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS so Flutter (Web/Emulator) can make HTTP requests


@app.route('/news.all.get')
def get_news_all_articles():
    # Construct an absolute path to news_data.json relative to this file
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, 'news_data.json')
    
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        app.logger.error(f"Error loading news data: {e}")
        return jsonify({"error": "Failed to load news data"}), 500


@app.route('/news.categories.get')
def get_news_categories():
    time_now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
        'title': 'List of Categories',
        'time': time_now_str,
        'categories': [
            {'id': 1, 'name': 'Sports'},
            {'id': 2, 'name': 'Politics'},
            {'id': 3, 'name': 'Education'}
        ]
    }
    return jsonify(data)


@app.route('/')
def index():
    return 'Welcome ENSIA Students from Flask!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
