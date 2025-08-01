import re
# Импортируем функции для работы с файлами из нашего же пакета
from . import file_handler

def highlight_keywords(text, keywords):
    for keyword in keywords:
        text = re.sub(f'({re.escape(keyword)})', r'\033[93m\1\033[0m', text, flags=re.IGNORECASE)
    return text

def search_articles(articles, query):
    file_handler.log_search_query(query)
    keywords = [kw.strip() for kw in query.lower().split()]
    found_articles = {}

    for title, data in articles.items():
        content = data.get('content', '').lower()
        title_lower = title.lower()
        
        if all(kw in title_lower or kw in content for kw in keywords):
            found_articles[title] = data

    return found_articles

def show_all_themes(articles):
    """Готовит отформатированный список всех тем."""
    if not articles:
        return "\nВ базе данных пока нет статей."
    
    output = "\n--- Все доступные темы ---\n"
    for i, title in enumerate(articles.keys(), 1):
        output += f"{i}. {title}\n"
    output += "--------------------------"
    return output

def add_article(articles):
    print("\n--- Добавление новой статьи ---")
    title = input("Введите заголовок новой статьи: ").strip()
    if not title:
        print("Заголовок не может быть пустым.")
        return

    if title.lower() in (t.lower() for t in articles.keys()):
        print("Статья с таким заголовком уже существует.")
        return

    description = input("Введите краткое описание статьи: ").strip()
    content = input("Введите полный текст статьи: ").strip()

    articles[title] = {"description": description, "content": content}
    file_handler.save_articles(articles)
    print(f"\nСтатья '{title}' успешно добавлена и сохранена!")

def find_similar_articles(articles, target_title):
    target_content = articles.get(target_title, {}).get('content', '').lower().split()
    if not target_content:
        return []

    similar = []
    for title, data in articles.items():
        if title == target_title:
            continue
        
        content = data.get('content', '').lower().split()
        common_words = set(target_content) & set(content)
        
        # Порог схожести можно настроить
        if len(common_words) > 3:
            similar.append(title)
            
    return similar