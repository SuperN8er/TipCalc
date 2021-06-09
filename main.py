"""practicing coding"""


def simple_add(x, y):
    print(x + y)


def calc_tax(bill):
    tax = bill * 0.08
    tax = round(tax, 2)
    print(f"tax: {tax}")
    return tax


def calc_tip(bill):
    tip = bill / 5
    tip = round(tip, 2)
    print(f"tip: {tip}")
    return tip


def calc_total(bill):
    tax_amt = calc_tax(bill)
    bill += tax_amt
    tip = calc_tip(bill)
    bill += tip
    print(f"total: {bill}")
    return bill


def main():
    # simple_add("tie ", "knot")
    bill = 100
    print(f"bill: {bill}")
    total = calc_total(bill)


if __name__ == "__main__":
    main()
