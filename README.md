# Lab 03 - Anticipating Change, Requirements & Design Models

## Run
```
python task1_likely_changes.py
python task2_library_model.py
python payments.py
pytest -v
```

## Task 2 - Library borrowing design (UML-style)
```
Library ──owns──> Book
   │──owns──> Member
   └──owns──> Loan ──> (Book, Member, due_date, returned)
```
Rule: one member can hold at most 3 books, loan period 14 days.

## Task 3 - Payment strategy diagram
```
Customer -> Checkout -> PaymentMethod
                        |-> CardPayment
                        |-> WalletPayment
                        |-> CashOnDelivery
```

## Task 4 - Rejected design alternative
I rejected a single `pay(amount, method)` function with `if method == "card" ... elif
method == "wallet" ...` branches.
Reason: every new payment method (wallet, COD, later maybe EasyPaisa/JazzCash) forces us
to edit the same function, which risks breaking the working card code and makes testing
harder. With composition (strategy objects behind a stable `PaymentMethod` boundary) a
new method is only a new class, and `Checkout` never changes (open/closed principle).
