class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_max(root):
    if root is None:
        return None

    current = root
    
    # Рухаємося до найправішого вузла, який містить максимальне значення.
    while current.right is not None:
        current = current.right

    return current.key

# Приклад використання (опціонально)
if __name__ == "__main__":
    # Створення простого дерева: 10 -> 20 -> 30 (max)
    root = Node(10)
    root.right = Node(20)
    root.right.right = Node(30)
    
    print(f"Максимальне значення: {find_max(root)}")
    
    