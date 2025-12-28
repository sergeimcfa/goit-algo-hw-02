from collections import deque

def is_palindrome(text):
    """
    Перевіряє, чи є рядок паліндромом, використовуючи deque.
    Ігнорує регістр та пробіли.
    """
    # Підготовка рядка: видаляємо пробіли та переводимо в нижній регістр
    # isalnum() залишає тільки букви та цифри, ігноруючи знаки пунктуації та пробіли
    processed_text = "".join(char.lower() for char in text if char.isalnum())
    
    char_deque = deque(processed_text)
    
    # Порівнюємо символи з обох кінців
    while len(char_deque) > 1:
        # popleft() бере з початку, pop() бере з кінця
        if char_deque.popleft() != char_deque.pop():
            return False
            
    return True

# Тестування
if __name__ == "__main__":
    test_strings = [
        "A man a plan a canal Panama",  # Паліндром
        "No lemon, no melon",          # Паліндром
        "Hello World",                 # Не паліндром
        "12321",                       # Паліндром
        "12345"                        # Не паліндром
    ]
    
    for s in test_strings:
        result = "Паліндром" if is_palindrome(s) else "Не паліндром"
        print(f"'{s}': {result}")
