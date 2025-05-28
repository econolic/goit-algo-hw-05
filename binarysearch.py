def binary_search_upper_bound(arr: list[float], target: float) -> tuple[int, float | None]:
    """
    Повертає (iterations, upper_bound) для верхньої межі target у впорядкованому списку arr.

    Parameters
    ----------
    arr : list[float]
        Впорядкований за зростанням список.
    target : float
        Значення для пошуку.

    Returns
    -------
    Tuple[int, Optional[float]]
        iterations – кількість ітерацій,
        upper_bound – мінімальний елемент ≥ target або None.
    """
    if not arr:
        raise ValueError("Input array must contain at least one element.")

    left, right = 0, len(arr) - 1
    iterations: int = 0
    candidate: float | None = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2
        mid_val = arr[mid]

        if mid_val >= target:
            candidate = mid_val
            right = mid - 1  # шукаємо ліву частину для меншого допустимого значення
        else:
            left = mid + 1

    return iterations, candidate

if __name__ == "__main__":
    # Тестуємо функцію binary_search_upper_bound
    arr = [1.0, 2.5, 3.0, 4.5, 5.0]
    target = 3.0
    iterations, upper_bound = binary_search_upper_bound(arr, target)
    
    print(f"Iterations: {iterations}, Upper Bound: {upper_bound}")  # Виведе: Iterations: 3, Upper Bound: 3.0
    assert iterations == 3
    assert upper_bound == 3.0

    # Тестуємо випадок, коли target більше за всі елементи
    target = 6.0
    iterations, upper_bound = binary_search_upper_bound(arr, target)
    
    print(f"Iterations: {iterations}, Upper Bound: {upper_bound}")  # Виведе: Iterations: 3, Upper Bound: None
    assert iterations == 3
    assert upper_bound is None