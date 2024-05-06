def merge_k_lists(lists):
    """Об'єднує кілька відсортованих списків у один відсортований список за допомогою мінімальної купи."""
    if not lists:
        return []  # повернення порожнього списку, якщо вхідний список пустий

    min_heap = []
    for i, lst in enumerate(lists):
        if lst:  # перевірка на порожній список у списку списків
            heapq.heappush(min_heap, (lst[0], i, 0))

    result = []
    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        if element_idx + 1 < len(lists[list_idx]):
            heapq.heappush(min_heap, (lists[list_idx][element_idx + 1], list_idx, element_idx + 1))

    return result


def user_interface():
    """Функція для взаємодії з користувачем та отримання списків для злиття."""
    import ast
    lists = []
    print("Введіть відсортовані списки один за одним. Введіть 'end' для завершення.")
    while True:
        user_input = input("Введіть список або 'end' для завершення: ")
        if user_input.lower() == 'end':
            break
        try:
            # Безпечне перетворення рядка вводу у список цілих чисел
            lst = ast.literal_eval(user_input)
            if isinstance(lst, list) and all(isinstance(x, int) for x in lst):
                lists.append(lst)
            else:
                print("Помилка: введіть коректний список цілих чисел.")
        except:
            print("Помилка: введіть коректний список цілих чисел.")

    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)

user_interface()
