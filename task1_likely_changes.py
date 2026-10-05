"""Lab 03 - Lab Task 1: Identify five likely changes in the food-delivery scenario."""

likely_changes = [
    {
        "change": "Add Wallet payment",
        "affected": "Payment module",
        "how_design_helps": "New class WalletPayment; Checkout stays unchanged",
    },
    {
        "change": "Add Cash-on-Delivery (COD)",
        "affected": "Payment module",
        "how_design_helps": "New class CashOnDelivery; Checkout stays unchanged",
    },
    {
        "change": "Delivery fee rules change (distance based / free above X)",
        "affected": "Fee calculation",
        "how_design_helps": "Fee logic is kept in one place, not mixed with payment",
    },
    {
        "change": "Add discount coupons / promo codes",
        "affected": "Order total calculation",
        "how_design_helps": "Total is computed in one function, coupon is plugged in",
    },
    {
        "change": "Change payment gateway provider (e.g. new card gateway)",
        "affected": "CardPayment implementation only",
        "how_design_helps": "Only the card class is edited, interface stays stable",
    },
]

if __name__ == "__main__":
    for i, item in enumerate(likely_changes, start=1):
        print(f"{i}. {item['change']}")
        print(f"   Affected : {item['affected']}")
        print(f"   Design   : {item['how_design_helps']}")
