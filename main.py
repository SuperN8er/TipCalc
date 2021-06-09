"""practicing coding"""


def simple_add(x, y):
    print(x + y)


def calc_tax(bill, tax_amt=0.08):
    tax = bill * tax_amt
    tax = round(tax, 2)
    print(f"tax: {tax}")
    return tax


def calc_tip(bill, tip_amt=0.18):
    tip = bill * tip_amt
    tip = round(tip, 2)
    print(f"tip: {tip}")
    return tip


def calc_total(bill):
    tax_amt = calc_tax(bill)
    bill += tax_amt
    tip = calc_tip(bill)
    bill += tip
    print(f"total: {bill}")


def main():
    # simple_add("tie ", "knot")
    bill = 100
    print(f"bill: {bill}")
    calc_total(bill)


if __name__ == "__main__":
    main()
