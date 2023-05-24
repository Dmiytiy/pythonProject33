import random

def create_orders(data):
    volume = data['volume']
    number = data['number']
    amount_dif = data['amountDif']
    side = data['side']
    price_min = data['priceMin']
    price_max = data['priceMax']

    total_volume = volume
    orders = []

    for _ in range(number):
        # Генерация случайной цены в заданном диапазоне
        price = random.uniform(price_min, price_max)

        # Генерация случайного объема в заданном разбросе
        volume_dif = random.uniform(-amount_dif, amount_dif)
        order_volume = volume / number + volume_dif

        # Создание ордера с полученными данными
        order = {
            'side': side,
            'price': price,
            'volume': order_volume
        }

        # Добавление ордера в список ордеров
        orders.append(order)

        # Обновление оставшегося объема
        total_volume -= order_volume

    # Проверка наличия неиспользованного объема
    if total_volume > 0:
        # Если остался неиспользованный объем, создаем дополнительный ордер с оставшимся объемом
        order = {
            'side': side,
            'price': random.uniform(price_min, price_max),
            'volume': total_volume
        }
        orders.append(order)

    return orders

# Тестирование функции
data = {
    'volume': 10000.0,
    'number': 5,
    'amountDif': 50.0,
    'side': 'SELL',
    'priceMin': 200.0,
    'priceMax': 300.0
}

orders = create_orders(data)
for order in orders:
    print(order)