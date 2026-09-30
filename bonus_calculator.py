from collections import defaultdict
from datetime import datetime


def calculate_bonus(users):
    """
    Функция рассчитывает бонус "Быстрый старт" для пользователей.

    :param users: список пользователей с их ID, реферером,
    купленным пакетом и датой покупки.
    """

    # Словари для хранения информации о пользователях и реферальных связях
    user_packages = {}  # ID пользователя -> (размер пакета, дата покупки)
    referrals = defaultdict(list)  # ID пользователя -> список его рефералов
    bonus_awarded = []  # Список пользователей, получивших бонус

    # Заполняем данные
    for user in users:
        user_id, referrer, package, purchase_date = (
            user["id"],
            user["referrer_id"],
            user["package"],
            user["purchase_date"],
        )
        user_packages[user_id] = (package, purchase_date)
        if referrer:
            referrals[referrer].append(user_id)

    # Проверяем выполнение условий бонуса
    for user_id, (package, purchase_date) in user_packages.items():
        # Минимальный пакет для начисления бонуса — 1500, игнорируем
        if package < 1500:
            continue

        # Фильтруем приглашенных рефералов с пакетом 1500+
        direct_refs = [
            ref
            for ref in referrals[user_id]
            if user_packages.get(ref, (0, None))[0] >= 1500
        ]

        if len(direct_refs) < 2:
            continue  # Нужно минимум 2 приглашенных реферала

        qualified_refs = 0  # Количество рефералов, выполнивших условия

        for ref in direct_refs:
            # Подсчитываем рефералов второго уровня
            sub_refs = [
                sub
                for sub in referrals[ref]
                if user_packages.get(sub, (0, None))[0] >= 1500
            ]
            if len(sub_refs) >= 2:
                qualified_refs += 1

        # Если 2 реферала выполнили условия
        # (под ними по 2 человека с пакетами 1500+)
        if qualified_refs >= 2:
            bonus_awarded.append((user_id, direct_refs))

    # Выводим список пользователей, получивших бонус
    for user_id, refs in bonus_awarded:
        # Преобразуем список рефералов в строку
        refs_str = ", ".join(map(str, refs))
        print(
            f"Пользователь c ID: {user_id} получил бонус!\n"
            f"Рефералы с ID: {refs_str}."
        )


# Пример данных пользователей
users = [
    {
        "id": 1,
        "referrer_id": None,
        "package": 3000,
        "purchase_date": datetime(2024, 5, 1),
    },
    {"id": 2, "referrer_id": 1, "package": 1500, "purchase_date": datetime(2024, 5, 2)},
    {"id": 3, "referrer_id": 1, "package": 1500, "purchase_date": datetime(2024, 5, 3)},
    {"id": 4, "referrer_id": 2, "package": 1500, "purchase_date": datetime(2024, 5, 4)},
    {"id": 5, "referrer_id": 2, "package": 1500, "purchase_date": datetime(2024, 5, 5)},
    {"id": 6, "referrer_id": 3, "package": 1500, "purchase_date": datetime(2024, 5, 6)},
    {"id": 7, "referrer_id": 3, "package": 1500, "purchase_date": datetime(2024, 5, 7)},
]

calculate_bonus(users)
