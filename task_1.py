from queue import Queue
import time
import random

# Створити чергу заявок
queue = Queue()

def generate_request():
    """Генерує нову заявку та додає її до черги."""
    # Генеруємо унікальний номер заявки (просто число для прикладу)
    request_id = random.randint(1000, 9999)
    print(f"Згенеровано заявку #{request_id}")
    queue.put(request_id)

def process_request():
    """Обробляє заявку, видаляючи її з черги."""
    if not queue.empty():
        # Отримуємо заявку з черги
        request_id = queue.get()
        print(f"Обробка заявки #{request_id}...")
        # Імітація часу обробки
        time.sleep(1) 
        print(f"Заявку #{request_id} оброблено.")
    else:
        print("Черга пуста. Немає заявок для обробки.")

def main():
    print("Система обробки заявок запущена. Натисніть Ctrl+C для виходу.")
    try:
        while True:
            # Імітуємо ймовірність появи нової заявки (50% шанс)
            if random.choice([True, False]):
                generate_request()
            
            # Спробуємо обробити заявку
            process_request()
            
            # Невелика пауза між ітераціями циклу
            time.sleep(0.5)
            print("-" * 20)
            
    except KeyboardInterrupt:
        print("\nРоботу програми завершено користувачем.")

if __name__ == "__main__":
    main()
