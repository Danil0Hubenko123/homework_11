## Клас Вузла для Двійкового Дерева Пошуку (BST)

class Node:
    """
    Реалізація вузла для двійкового дерева пошуку (BST) або AVL-дерева.
    Кожен вузол містить ключ, а також посилання на лівого та правого нащадків.
    """
    def __init__(self, key):
        self.key = key  # Значення, що зберігається у вузлі
        self.left = None # Ліве піддерево (менші значення)
        self.right = None # Праве піддерево (більші значення)

    def __str__(self):
        return f"Node({self.key})"


## Функція 1: Пошук мінімального значення (Ітеративно)

def find_min_value_iterative(root):
    """
    Знаходить найменше значення у дереві, рухаючись постійно до найлівішого вузла.
    Це стандартний і рекомендований підхід для BST/AVL.
    
    Складність: O(h), де h - висота дерева.
    
    Аргументи:
        root (Node): Корінь дерева.
        
    Повертає:
        int/float: Найменше значення у дереві, або None, якщо дерево порожнє.
    """
    # Перевірка на порожнє дерево
    if root is None:
        return None
    
    current = root
    
    # Поки існує лівий нащадок, продовжуємо рухатися вліво
    while current.left is not None:
        current = current.left
        
    # Знайдено найбільш лівий вузол, повертаємо його ключ
    return current.key


## Функція 2: Пошук мінімального значення (Рекурсивно)

def find_min_value_recursive(node):
    """
    Знаходить найменше значення рекурсивно.
    
    Складність: O(h), де h - висота дерева.
    
    Аргументи:
        node (Node): Поточний вузол.
        
    Повертає:
        int/float: Найменше значення, або None, якщо дерево порожнє.
    """
    # Базовий випадок 1: Дерево порожнє
    if node is None:
        return None
    
    # Базовий випадок 2: Знайшли найбільш лівий вузол (ключ мінімальний)
    if node.left is None:
        return node.key
    
    # Рекурсивний крок: продовжуємо пошук у лівому піддереві
    return find_min_value_recursive(node.left)


## Приклад використання

if __name__ == "__main__":
    print("--- Тестування функцій пошуку мінімального значення у BST/AVL ---")
    
    # Створення тестового дерева:
    #         20
    #        /  \
    #      10    30
    #     / \   /
    #    5  15 25
    #   /
    #  2  <-- Мінімальне значення
    
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)
    root.right.left = Node(25)
    root.left.left.left = Node(2)

    print("\nСтворено дерево (найменший елемент: 2)")

    # 1. Тест ітеративної функції
    min_iterative = find_min_value_iterative(root)
    print(f"\n1. Результат ітеративного пошуку: {min_iterative}")
    
    # 2. Тест рекурсивної функції
    min_recursive = find_min_value_recursive(root)
    print(f"2. Результат рекурсивного пошуку: {min_recursive}")
    
    # Тест на порожньому дереві
    min_empty = find_min_value_iterative(None)
    print(f"\nТест на порожньому дереві: {min_empty}")
    
    