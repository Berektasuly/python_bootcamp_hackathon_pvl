from app.file_handler import load_articles, save_articles
from app.ui import run_app

def main():
    """Главная функция для запуска приложения."""
    # Пытаемся загрузить статьи из файла articles.json
    articles = load_articles()
    
    # Если файл не был найден или он пуст, articles будет пустым словарем.
    # В этом случае - и только в этом - мы создаем базу по умолчанию.
    if not articles:
        articles = initialize_database()
    
    # Запускаем основной цикл приложения с загруженными (или созданными) статьями
    run_app(articles)

# Эта строка гарантирует, что функция main() запустится только тогда,
# когда этот файл исполняется напрямую.
if __name__ == "__main__":
    main()