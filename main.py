def input_data():
    """Функция для ввода исходных данных"""
    print("Нажмите '1' для ручного ввода")
    
    choice = input()
    
    if choice == "1":
        return manual_input()
    else:
        print("Неверный выбор. Возврат в главное меню.")
        return None

def manual_input():
    """Ручной ввод текста и строки для поиска"""
    text = input("Введите текст: ")
    search_string = input("Введите строку для поиска: ")
    return {"text": text, "search_string": search_string}

def process_algorithm(data):
    """Функция для выполнения алгоритма"""
    text = data["text"]
    search_string = data["search_string"]
    
    # Разбиваем текст на слова
    words = text.split()
    
    # Ищем слова, содержащие подстроку
    result_words = []
    for word in words:
        if search_string.lower() in word.lower():
            result_words.append(word)
    
    return result_words

def output_result(result):
    """Функция для вывода результата"""
    if not result:
        print("Слова, содержащие указанную подстроку, не найдены.")
    else:
        print("Найденные слова:", ", ".join(result))

def main():
    """Главная функция приложения"""
    current_data = None
    current_result = None
    
    while True:
        print("\n1. Ввод исходных данных")
        print("2. Выполнение алгоритма")
        print("3. Вывод результата")
        print("4. Завершение работы")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == "1":
            current_data = input_data()
            current_result = None  # Сбрасываем результаты при вводе новых данных
        elif choice == "2":
            if current_data is None:
                print("Ошибка: Сначала введите данные!")
            else:
                current_result = process_algorithm(current_data)
                print("Алгоритм выполнен успешно!")
        elif choice == "3":
            if current_result is None:
                print("Ошибка: Сначала выполните алгоритм!")
            else:
                output_result(current_result)
        elif choice == "4":
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()