from typing import Any

class Deque:

    def __init__(self) -> None:
        self.__items: list[Any] = []

    def is_empty(self) -> bool:
        return len(self.__items) == 0

    def size(self) -> int:
        return len(self.__items)

    def insert_last(self, valor: Any) -> None:
        self.__items.append(valor)

    def insert_first(self, valor: Any) -> None:
        self.__items.insert(0, valor)

    def first(self) -> Any:
        if self.is_empty():
            print("Aviso: Deque vazio. Não há primeiro elemento.")
            return None
        return self.__items[0]

    def remove_last(self) -> Any:
        if self.is_empty():
            print("Erro: Tentativa de remover do fim de um Deque vazio.")
            return None
        return self.__items.pop()

    def last(self) -> Any:
        if self.is_empty():
            print("Aviso: Deque vazio. Não há último elemento.")
            return None
        return self.__items[-1]

    def remove_first(self) -> Any:
        if self.is_empty():
            print("Erro: Tentativa de remover do início de um Deque vazio.")
            return None
        return self.__items.pop(0)

    def __repr__(self) -> str:
        return f"Deque({self.__items})"


if __name__ == "__main__":
    print("--- Iniciando testes do Deque ---")
    d = Deque()

    print("Operação 1: insert_last(10)")
    d.insert_last(10)
    print(d)

    print("\nOperação 2: insert_first(5)")
    d.insert_first(5)
    print(d)

    print("\nOperação 3: insert_last(20)")
    d.insert_last(20)
    print(d)

    print(f"\nOperação 4: Tamanho atual = {d.size()}")

    print(f"Operação 5: Primeiro: {d.first()}, Último: {d.last()}")

    print(f"\nOperação 6: remove_first() -> {d.remove_first()}")
    print(d)

    print(f"Operação 7: remove_last() -> {d.remove_last()}")
    print(d)

    print("\nOperação 8: insert_first(15)")
    d.insert_first(15)
    print(d)

    print(f"Operação 9: remove_first() -> {d.remove_first()}")
    print(f"Operação 10: remove_last() -> {d.remove_last()}")
    print(f"Está vazio? {d.is_empty()}")

    print("\nOperação extra (Tratamento de erro): Tentando remover de deque vazio")
    d.remove_first()
    d.remove_last()