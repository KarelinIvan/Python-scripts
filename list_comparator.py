from typing import List


def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    """Функция находит индексы элемнотов первого списка, которые меньше
    элементов второго списка.
    Возвращает список индексов.
    """
    list_indices = []

    for k, v in enumerate(zip(nums1, nums2)):
        if nums1[k] < nums2[k]:
            list_indices.append(k)
    return list_indices
