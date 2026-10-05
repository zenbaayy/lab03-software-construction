"""Lab 03 - Lab Task 5: Tests proving the client works with both strategies."""

import pytest

from payments import CardPayment, CashOnDelivery, Checkout, WalletPayment


@pytest.mark.parametrize(
    "method, expected",
    [
        (CardPayment(), "Card charged: 2500.00"),
        (WalletPayment(balance=5000), "Wallet debited: 2500.00"),
        (CashOnDelivery(), "Cash to be collected on delivery: 2500.00"),
    ],
)
def test_checkout_works_with_every_strategy(method, expected):
    assert Checkout(method).pay(2500) == expected


def test_wallet_balance_is_reduced():
    wallet = WalletPayment(balance=1000)
    Checkout(wallet).pay(400)
    assert wallet.balance == 600


def test_wallet_insufficient_balance_rejected():
    with pytest.raises(ValueError):
        Checkout(WalletPayment(balance=100)).pay(500)


@pytest.mark.parametrize(
    "method", [CardPayment(), WalletPayment(100), CashOnDelivery()]
)
@pytest.mark.parametrize("bad_amount", [0, -5])
def test_non_positive_amount_rejected(method, bad_amount):
    with pytest.raises(ValueError):
        Checkout(method).pay(bad_amount)
