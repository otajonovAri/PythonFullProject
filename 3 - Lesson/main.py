print()
print("Example 1")
price = float(input("Enter the product price: "))
discount_percent = float(input("Enter the discount percentage: "))
discount_amount = price * (discount_percent / 100)
new_price = price - discount_amount
print(f"\nDiscount: {int(discount_amount)} so'm")
print(f"New price: {int(new_price)} so'm")

print()
print("Example 2")
import math
a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))
perimeter = a + b + c
s = perimeter / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"\nPerimeter: {perimeter}")
print(f"Area: {area:.4f}")

print()
print("Example 3")
loan_amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (%): "))
loan_term = int(input("Enter the loan term (in years): "))
annual_interest = loan_amount * (annual_interest_rate / 100)
total_debt = loan_amount + (annual_interest * loan_term)
print(f"\nAnnual interest: {int(annual_interest)}")
print(f"Total debt amount: {int(total_debt)}")
