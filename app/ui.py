# Импортируем модули с логикой из нашего пакета
from . import article_manager

def print_menu():
    # Выводит меню приложения
    print("\n--- Меню Поисковика по Википедии ---")
    print("1. Поиск статьи")
    print("2. Показать все темы")
    print("3. Добавить новую статью")
    print("Введите 'выход' для завершения работы.")
    print("-------------------------------------")
# Функция для запуска приложения
# Принимает словарь статей и предоставляет интерфейс для взаимодействия с пользователем
def run_app(articles):
    print("Добро пожаловать в поисковик по Википедии!")
    print("Есть инструкция при запуске (что можно делать).")
    # Основной цикл приложения
    # Позволяет пользователю выбирать действия из меню
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
# Функция для обработки поиска статей
def handle_search(articles):
    # Обрабатывает поиск статей по ключевым словам
    print("\n--- Поиск статьи ---")
    # Запрашиваем у пользователя ключевое слово для поиска
    # Если пользователь ввел пустой запрос, выводим сообщение и возвращаемся в меню
    query = input("Введите ключевое слово для поиска: ").strip()
    # Проверяем, что запрос не пустой
    if not query:
        print("Запрос не может быть пустым.")
        return
    # Ищем статьи по ключевым словам
    # Используем функцию из article_manager для поиска
    found = article_manager.search_articles(articles, query)
    # Если статьи не найдены, выводим сообщение и возвращаемся в меню
    if not found:
        print("\nНичего не найдено. Попробуйте другой запрос.")
        return
    # Если статьи найдены, выводим их заголовки
    print(f"\n--- Найдено статей: {len(found)} ---")
    # Перебираем найденные статьи и выводим их заголовки
    found_list = list(found.items())
    # Используем enumerate для нумерации статей
    for i, (title, data) in enumerate(found_list, 1):
        # Выводим номер статьи и заголовок
        print(f"{i}. {title}")
    
    try:
        # Запрашиваем у пользователя номер статьи для просмотра
        # Если пользователь ввел 'назад', возвращаемся в меню
        article_num_str = input("Введите номер статьи для просмотра или 'назад' для возврата в меню: ").strip()
        if article_num_str.lower() == 'назад':
            return
        # Преобразуем введенный номер в целое число
        # Если введено некорректное значение, выводим сообщение об ошибке
        article_index = int(article_num_str) - 1
        if 0 <= article_index < len(found_list):
            title, data = found_list[article_index]
            # Выводим заголовок статьи и ее содержимое
            print(f"\n--- {title} ---")
            if 'description' in data:
                # Если есть краткое описание, выводим его
                print(f"\nКраткое описание: {data['description']}\n")
            # Подсвечиваем ключевые слова в содержимом статьи
            content = data.get('content', 'Содержимое отсутствует.')
            # Разбиваем запрос на ключевые слова для подсветки
            keywords_to_highlight = query.lower().split()
            # Используем функцию из article_manager для подсветки ключевых слов
            highlighted_content = article_manager.highlight_keywords(content, keywords_to_highlight)
            # Выводим содержимое статьи с подсветкой ключевых слов
            print(highlighted_content)
            # Если есть содержимое статьи, ищем похожие статьи
            similar = article_manager.find_similar_articles(articles, title)
            if similar:
                print("\nПохожие статьи:")
                # Выводим заголовки похожих статей s_titles - список заголовков, similar - список похожих статей
                for s_title in similar:
                    print(f"- {s_title}")
        else:
            print("Неверный номер статьи.")
    except ValueError:
        print("Пожалуйста, введите корректный номер.")