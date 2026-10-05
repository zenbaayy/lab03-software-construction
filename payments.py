"""Lab 03 - Lab Task 3: Two (actually three) interchangeable payment strategies."""

from typing import Protocol


class PaymentMethod(Protocol):
    """Stable boundary: Checkout only depends on this behaviour."""

    def pay(self, amount: float) -> str: ...


class CardPayment:
    def pay(self, amount: float) -> str:
        _validate(amount)
        return f"Card charged: {amount:.2f}"


class WalletPayment:
    def __init__(self, balance: float = 0.0):
        self.balance = balance

    def pay(self, amount: float) -> str:
        _validate(amount)
        if amount > self.balance:
            raise ValueError("Insufficient wallet balance")
        self.balance -= amount
        return f"Wallet debited: {amount:.2f}"


class CashOnDelivery:
    def pay(self, amount: float) -> str:
        _validate(amount)
        return f"Cash to be collected on delivery: {amount:.2f}"


def _validate(amount: float) -> None:
    if amount <= 0:
        raise ValueError("Amount must be positive")


class Checkout:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def pay(self, amount: float) -> str:
        return self.payment_method.pay(amount)


if __name__ == "__main__":
    for method in (CardPayment(), WalletPayment(5000), CashOnDelivery()):
        print(Checkout(method).pay(2500))
