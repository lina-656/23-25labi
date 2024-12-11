#обычная реализация кода 
def print_menu():
    """Выводит меню с доступными заданиями."""
    print("\nМеню:")
    print("1. Ввод исходных данных")
    print("2. Выполнение алгоритма")
    print("3. Вывод результата")
    print("4. Завершение работы программы")

def input_data():
    """Вводит строку и величину сдвига от пользователя."""
    text = input("Введите строку для шифрования: ")
    shift = int(input("Введите величину сдвига: "))
    return text, shift

def vigenere_cipher(text, shift):
    """Шифрует строку с помощью шифра Вижинера."""
    encrypted_text = []
    shift = shift % 26  # Обеспечиваем корректный сдвиг в пределах алфавита

    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            # Сдвигаем символ
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Не изменяем не буквенные символы

    return ''.join(encrypted_text)

def main():
    """Основная функция программы, которая управляет выбором задания пользователем."""
    text = None
    shift = None
    result = None

    while True:
        print_menu()  # Выводим меню
        choice = input("Выберите пункт меню: ")  # Запрашиваем выбор пользователя

        if choice == '1':
            # Ввод исходных данных
            text, shift = input_data()
            result = None  # Сбрасываем результат

        elif choice == '2':
            # Выполнение алгоритма
            if text is not None and shift is not None:
                result = vigenere_cipher(text, shift)
                print("Алгоритм выполнен.")
            else:
                print("Сначала введите данные.")

        elif choice == '3':
            # Вывод результата
            if result is not None:
                print("Зашифрованная строка:")
                print(result)
            else:
                print("Результаты отсутствуют. Выполните алгоритм.")

        elif choice == '4':
            print("Завершение работы программы.")  # Сообщаем о завершении
            break  # Выходим из цикла

        else:
            print("Неверный выбор.")  # Обработка неверного выбора

if __name__ == "__main__":
    main()  # Запуск основной функции при выполнении скрипта
