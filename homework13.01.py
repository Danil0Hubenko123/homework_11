import heapq
from typing import List

def min_cost_to_connect_cables(cable_lengths: List[int]) -> int:
    if not cable_lengths or len(cable_lengths) < 2:
        return 0

    heapq.heapify(cable_lengths)
    
    total_cost = 0

    while len(cable_lengths) > 1:
        cable1 = heapq.heappop(cable_lengths)
        cable2 = heapq.heappop(cable_lengths)

        cost = cable1 + cable2

        total_cost += cost

        heapq.heappush(cable_lengths, cost)

    return total_cost

def merge_k_lists(lists: List[List[int]]) -> List[int]:
    min_heap = []
    result = []

    for list_index, current_list in enumerate(lists):
        if current_list:
            heapq.heappush(min_heap, (current_list[0], list_index, 0))

    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        result.append(value)

        next_element_index = element_index + 1
        current_list = lists[list_index]

        if next_element_index < len(current_list):
            heapq.heappush(min_heap, (
                current_list[next_element_index],
                list_index,
                next_element_index
            ))

    return result

if __name__ == '__main__':
    print("ЧАСТИНА 1: Мінімальна вартість об'єднання кабелів")
    cables = [4, 3, 2, 6]
    cost = min_cost_to_connect_cables(cables.copy()) # Використовуємо копію, бо функція змінює список
    print(f"Довжини кабелів: {cables}")
    print(f"Мінімальна загальна вартість: {cost}")
    
    print("-" * 50)

    cables_2 = [1, 2, 5, 10, 3]
    cost_2 = min_cost_to_connect_cables(cables_2.copy())
    print(f"Довжини кабелів: {cables_2}")
    print(f"Мінімальна загальна вартість: {cost_2}")
    
    print("-" * 50)

    print("ЧАСТИНА 2: Об'єднання k відсортованих списків")
    lists = [[1, 4, 5], [1, 3, 4], [2, 6], [0, 8, 9]]
    merged_list = merge_k_lists(lists)
    print(f"Вхідні списки: {lists}")
    print(f"Відсортований список: {merged_list}")

    print("-" * 50)

    lists_2 = [[10, 20], [1, 5, 15], [30]]
    merged_list_2 = merge_k_lists(lists_2)
    print(f"Вхідні списки: {lists_2}")
    print(f"Відсортований список: {merged_list_2}")
    
    