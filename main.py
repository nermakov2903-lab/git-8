
def input_data():
    """Функция для ввода исходных данных"""
    pass

def process_algorithm(data):
    """Функция для выполнения алгоритма"""
    pass

def output_result(result):
    """Функция для вывода результата"""
   pass

def main():
    """Главная функция приложения"""
    current_data = None
    current_result = None
    
    while True:
        print("1. Ввод исходных данных")
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