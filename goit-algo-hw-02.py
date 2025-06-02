import queue
import random
import time

# Створення черги заявок
request_queue = queue.Queue()

def generate_request():
    """Генерує нову заявку та додає її до черги."""
    request_id = random.randint(1000, 9999)  # Унікальний номер заявки
    request_queue.put(request_id)
    print(f"Заявка {request_id} додана до черги.")

def process_request():
    """Обробляє заявку, видаляючи її з черги."""
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Заявка {request_id} оброблена.")
    else:
        print("Черга пуста. Немає заявок для обробки.")

def main():
    """Головний цикл програми."""
    while True:
        action = input("Введіть 'g' для генерації заявки, 'p' для обробки заявки, 'q' для виходу: ").lower()
        if action == 'g':
            generate_request()
        elif action == 'p':
            process_request()
        elif action == 'q':
            print("Завершення роботи.")
            break
        else:
            print("Невірний ввід. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
