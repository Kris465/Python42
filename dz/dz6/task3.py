def get_operator_rate(operator):
    rates = {
        "МТС": 1.5,      # Тариф для МТС (русский)
        "Билайн": 1.2,   # Тариф для Билайн
        "Мегафон": 1.3,  # Тариф для Мегафон
        "T2": 1.1     # Тариф для T2 (английский)
    }
    return rates.get(operator, None)


def calculate_cost(call_duration, from_operator, to_operator):
    from_rate = get_operator_rate(from_operator)
    to_rate = get_operator_rate(to_operator)

    if from_rate is None or to_rate is None:
        return None

    total_cost = call_duration * from_rate * to_rate
    return total_cost


def main():
    print("Доступные операторы: МТС, Билайн, Мегафон, T2")

    call_duration = float(input("Введите длительность разговора в минутах: "))
    from_operator = input("Введите оператора, с которого звоните: ")
    to_operator = input("Введите оператора, на которого звоните: ")

    cost = calculate_cost(call_duration, from_operator, to_operator)

    if cost is not None:
        print(f"Стоимость разговора с {from_operator} на {to_operator}: ",
              end='')
        print(f"{cost:.2f} рублей")
    else:
        print("Ошибка: Неверный оператор.")


if __name__ == "__main__":
    main()
