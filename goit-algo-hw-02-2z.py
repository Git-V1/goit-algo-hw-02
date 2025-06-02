from collections import deque

def is_palindrome(s):
    """Перевіряє, чи є рядок паліндромом."""
    s = ''.join(s.lower().split())  # Змінюємо регістр і видаляємо пробіли
    char_deque = deque(s)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Тестування функції
test_strings = [
    "Закат таказ",
    "Мадам",
    "не паліндром",
    "А роза упала на лапу Азора"
]

for test in test_strings:
    print(f"Рядок '{test}' є паліндромом: {is_palindrome(test)}")
