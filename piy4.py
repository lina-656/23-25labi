#реализация программы с паттером state (основная программа)
from state import Context # type: ignore

def print_menu():
    """Выводит меню с доступными заданиями."""
    print("\nМеню:")
    print("1. Ввод исходных данных")
    print("2. Выполнение алгоритма")
    print("3. Вывод результата")
    print("4. Завершение работы программы")

def vigenere_cipher(text, shift):
    """Шифрует строку с помощью шифра Вижинера."""
    encrypted_text = []
    shift = shift % 26  # Обеспечиваем корректный сдвиг в пределах алфавита

    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Не изменяем не буквенные символы

    return ''.join(encrypted_text)

def main():
    """Основная функция программы, которая управляет выбором задания пользователем."""
    context = Context()

    while True:
        print_menu()  # Выводим меню
        choice = input("Выберите пункт меню: ")  # Запрашиваем выбор пользователя

        if choice == '1':
            # Ввод исходных данных
            context.input_data()

        elif choice == '2':
            # Выполнение алгоритма
            context.execute_algorithm()

        elif choice == '3':
            # Вывод результата
            context.output_result()

        elif choice == '4':
            print("Завершение работы программы.")  # Сообщаем о завершении
            break  # Выходим из цикла

        else:
            print("Неверный выбор.")  # Обработка неверного выбора

if __name__ == "__main__":
    main()  # Запуск основной функции при выполнении скрипта
