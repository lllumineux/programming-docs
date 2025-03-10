# Интерфейс стратегии
class Payment:
    def pay(self, amount: float) -> bool:
        pass


# Конкретная стратегия #1
class CardPayment(Payment):
    def __init__(self, number: str, cvc: str, exp_date: str):
        self.card_number = number
        self.cvv = cvc
        self.expiration_date = exp_date

    def pay(self, amount: float) -> bool:
        # ...
        return True


# Конкретная стратегия #2
class CashAppPayment(Payment):
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    def pay(self, amount: float) -> bool:
        # ...
        return True


# Конкретная стратегия #3
class CryptoPayment(Payment):
    def __init__(self, address: str):
        self.wallet_address = address

    def pay(self, amount: float) -> bool:
        # ...
        return True


# Контекст
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None

    def set_payment_strategy(self, strategy: Payment):
        self.payment_strategy = strategy

    def add_item(self, item: str, price: float):
        self.items.append((item, price))

    def checkout(self):
        total_amount = sum(price for _, price in self.items)
        if self.payment_strategy.pay(total_amount):
            self.items = []
        else:
            raise ValueError

#  Клиентский код
def main():
    cart = ShoppingCart()
    cart.add_item('Ноутбук', 75000)
    cart.add_item('Наушники', 15000)
    
    strategy = CardPayment('1234-5678-9012-3456', '123', '12/25')
    # Не нужно знать заранее способ оплаты - можем динамически поставить любой 
    cart.set_payment_strategy(strategy)
    cart.checkout()
