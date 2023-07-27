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

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.transaction_count = 0
        self.operations = []

    def deposit(self, amount):
        self.operations.append({"тип": "пополнение", "сумма": amount})
        self.balance += amount

    def withdrawal(self, amount):
        self.operations.append({"тип": "снятие", "сумма": amount})
        self.balance -= amount

    def calculate_interest(self):
        return self.balance * 0.03

    def calculate_withdrawal_fee(self, amount):
        return min(max(amount * 0.015, 30), 600)

    def calculate_wealth_tax(self):
        return self.balance * 0.1

    def print_operations(self):
        for operation in self.operations:
            print(f"Тип: {operation['тип']}, Сумма: {operation['сумма']}")

    def atm(self):
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

                self.deposit(amount)
                self.transaction_count += 1

                if self.transaction_count % 3 == 0:
                    interest = self.calculate_interest()
                    self.deposit(interest)

                if self.balance > 5000000:
                    wealth_tax = self.calculate_wealth_tax()
                    self.balance -= wealth_tax

            elif choice == "2":
                amount = int(input("Введите сумму для снятия: "))

                if amount % 50 != 0:
                    print("Сумма снятия должна быть кратна 50 у.е.")
                    continue

                if amount > self.balance:
                    print("Недостаточно средств на счете")
                    continue

                self.withdrawal(amount)
                self.transaction_count += 1

                if self.transaction_count % 3 == 0:
                    interest = self.calculate_interest()
                    self.deposit(interest)

                withdrawal_fee = self.calculate_withdrawal_fee(amount)
                self.balance -= withdrawal_fee

                if self.balance > 5000000:
                    wealth_tax = self.calculate_wealth_tax()
                    self.balance -= wealth_tax

            elif choice == "3":

                break

            print("Сумма денег на счете:", self.balance)
        print("Список всех операций:")
        self.print_operations()


account = BankAccount()
account.atm()
