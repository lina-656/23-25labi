#реализация программы с паттером state (интерфейс и реализации состояний)
from piy import vigenere_cipher


class State:
    """Базовый интерфейс состояния."""
    def input_data(self, context):
        raise NotImplementedError

    def execute_algorithm(self, context):
        raise NotImplementedError

    def output_result(self, context):
        raise NotImplementedError

class InputDataState(State):
    """Состояние ввода данных."""
    def input_data(self, context):
        text = input("Введите строку для шифрования: ")
        shift = int(input("Введите величину сдвига: "))
        context.text = text
        context.shift = shift
        context.set_state(AlgorithmState())  # Переход к следующему состоянию

class AlgorithmState(State):
    """Состояние выполнения алгоритма."""
    def execute_algorithm(self, context):
        if context.text is not None and context.shift is not None:
            context.result = vigenere_cipher(context.text, context.shift)
            print("Алгоритм выполнен.")
            context.set_state(OutputResultState())  # Переход к следующему состоянию
        else:
            print("Сначала введите данные.")

class OutputResultState(State):
    """Состояние вывода результата."""
    def output_result(self, context):
        if context.result is not None:
            print("Зашифрованная строка:")
            print(context.result)
            context.set_state(InputDataState())  # Возврат к состоянию ввода данных
        else:
            print("Результаты отсутствуют. Выполните алгоритм.")

class Context:
    """Контекст для управления состоянием."""
    def __init__(self):
        self.state = InputDataState()  # Начальное состояние
        self.text = None
        self.shift = None
        self.result = None

    def set_state(self, state):
        self.state = state

    def input_data(self):
        self.state.input_data(self)

    def execute_algorithm(self):
        self.state.execute_algorithm(self)

    def output_result(self):
        self.state.output_result(self)
