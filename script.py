tickets = int(input("Введите количество билетов, которые хотите приобрести: "))
tickets_saved = tickets # сохранение количества билетов
tickets_sum = 0
while tickets > 0:
    age = int(input("Введите возраст участника конференции: "))
    if age < 18:
        tickets_sum = tickets_sum + 0
    elif 18 <= age < 25:
        tickets_sum = tickets_sum + 990
    elif age >= 25:
        tickets_sum = tickets_sum + 1390
    tickets = tickets - 1

if tickets_saved > 3:
    tickets_sum = tickets_sum - tickets_sum * 0.1
    print("Итоговая сумма со скидкой: ", tickets_sum)
else:
    print("Итоговая сумма: ", tickets_sum)
