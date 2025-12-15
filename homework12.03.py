class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def tree_sum(root: Node) -> int:
    if root is None:
        return 0

    # Рекурсивний крок: Сума = Поточний + Ліве піддерево + Праве піддерево
    return root.key + tree_sum(root.left) + tree_sum(root.right)

# Приклад використання
if __name__ == "__main__":
    # Створення дерева: 1 -> 2 (лівий), 3 (правий)
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    
    print(f"Сума всіх значень у дереві: {tree_sum(root)}")  # Очікується 6