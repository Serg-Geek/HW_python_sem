# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


def deposit(amount):
    operations.append({"тип": "deposit", "сумма": amount})
    # Дополнительный код для выполнения операции поступления средств

def withdrawal(amount):
    operations.append({"тип": "withdrawal", "сумма": amount})
    # Дополнительный код для выполнения операции снятия средств

def calculate_interest(balance):
    return balance * 0.03

def calculate_withdrawal_fee(amount):
    return min(max(amount * 0.015, 30), 600)

def calculate_wealth_tax(balance):
    return balance * 0.1

def print_operations():
    for operation in operations:
        print(f"Тип: {operation['тип']}, Сумма: {operation['сумма']}")

def atm():
    balance = 0
    transaction_count = 0
    wealth_tax = 0

    while True:
        print("Доступные действия:")
        print("1. Пополнить")
        print("2. Снять")
        print("3. Выйти")

        choice = input("Выберите действие (1-3): ")

        if choice == "1":
            amount = int(input("Введите сумму для пополнения: "))

            if amount % 50 != 0:
                print("Сумма пополнения должна быть кратна 50 у.е.")
                continue

            balance += amount
            transaction_count += 1

            if transaction_count % 3 == 0:
                interest = calculate_interest(balance)
                balance += interest

            if balance > 5000000:
                wealth_tax = calculate_wealth_tax(balance)
                balance -= wealth_tax

            deposit(amount)

        elif choice == "2":
            amount = int(input("Введите сумму для снятия: "))

            if amount % 50 != 0:
                print("Сумма снятия должна быть кратна 50 у.е.")
                continue

            if amount > balance:
                print("Недостаточно средств на счете")
                continue

            transaction_count += 1

            if transaction_count % 3 == 0:
                interest = calculate_interest(balance)
                balance += interest

            withdrawal_fee = calculate_withdrawal_fee(amount)
            balance -= amount + withdrawal_fee

            if balance > 5000000:
                wealth_tax = calculate_wealth_tax(balance)
                balance -= wealth_tax

            withdrawal(amount)

        elif choice == "3":
            break

        print("Сумма денег на счете:", balance)

    print("Список всех операций:")
    print_operations()

operations = []

atm()


