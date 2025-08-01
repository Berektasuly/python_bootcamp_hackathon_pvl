# Импортируем модули с логикой из нашего пакета
from . import article_manager

def print_menu():
    """Выводит главное меню."""
    print("\n--- Меню Поисковика по Википедии ---")
    print("1. Поиск статьи")
    print("2. Показать все темы")
    print("3. Добавить новую статью")
    print("Введите 'выход' для завершения работы.")
    print("-------------------------------------")

def run_app(articles):
    """Запускает главный цикл приложения."""
    print("Добро пожаловать в фейковый поисковик по Википедии!")
    print("Есть инструкция при запуске (что можно делать).")

    while True:
        print_menu()
        choice = input("Выберите действие или введите 'выход': ").strip().lower()

        if choice == 'выход':
            print("До свидания!")
            break
        
        elif choice == '1':
            handle_search(articles)
            
        elif choice == '2':
            print(article_manager.show_all_themes(articles))
            
        elif choice == '3':
            article_manager.add_article(articles)
            
        else:
            print("Неизвестная команда. Пожалуйста, выберите действие из меню.")

def handle_search(articles):
    """Обрабатывает логику поиска и вывода результатов."""
    query = input("Введите ключевое слово для поиска: ").strip()
    if not query:
        print("Запрос не может быть пустым.")
        return

    found = article_manager.search_articles(articles, query)

    if not found:
        print("\nНичего не найдено. Попробуйте другой запрос.")
        return

    print(f"\n--- Найдено статей: {len(found)} ---")
    found_list = list(found.items())
    for i, (title, data) in enumerate(found_list, 1):
        print(f"{i}. {title}")
    
    try:
        article_num_str = input("Введите номер статьи для просмотра или 'назад' для возврата в меню: ").strip()
        if article_num_str.lower() == 'назад':
            return
            
        article_index = int(article_num_str) - 1
        if 0 <= article_index < len(found_list):
            title, data = found_list[article_index]
            
            print(f"\n--- {title} ---")
            if 'description' in data:
                print(f"\nКраткое описание: {data['description']}\n")
                
            content = data.get('content', 'Содержимое отсутствует.')
            keywords_to_highlight = query.lower().split()
            highlighted_content = article_manager.highlight_keywords(content, keywords_to_highlight)
            print(highlighted_content)
            
            similar = article_manager.find_similar_articles(articles, title)
            if similar:
                print("\nПохожие статьи:")
                for s_title in similar:
                    print(f"- {s_title}")
        else:
            print("Неверный номер статьи.")
    except ValueError:
        print("Пожалуйста, введите корректный номер.")