import json
import os

DB_FILE = "articles.json"
LOG_FILE = "search_history.log"

def load_articles():
    if not os.path.exists(DB_FILE):
        return {}
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка при чтении файла {DB_FILE}: {e}")
        return {}

def save_articles(articles):
    try:
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(articles, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка при сохранении файла {DB_FILE}: {e}")

def log_search_query(query):
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(query + '\n')
    except IOError as e:
        print(f"Ошибка при записи в лог-файл {LOG_FILE}: {e}")