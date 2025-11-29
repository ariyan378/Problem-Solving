#Cash_in_hand

ctc = float(input("Enter Your annual salary (in Rs): "))

# Deductions
hra = ctc * 0.10
da  = ctc * 0.05
pf  = ctc * 0.03

salary_after = ctc - (hra + da + pf)

# Tax slabs
if salary_after < 5_00_000:
    tax = 0
elif salary_after < 10_00_000:
    tax = salary_after * 0.10
elif salary_after < 20_00_000:
    tax = salary_after * 0.20
else:
    tax = salary_after * 0.30

in_hand_salary = int(salary_after - tax)
monthly_in_hand = int(in_hand_salary / 12)

# Printing results
print(f"HRA deduction: {hra}")
print(f"DA deduction: {da}")
print(f"PF deduction: {pf}")
print(f"Tax deducted: {tax}")
print(f"Your annual in-hand salary: {in_hand_salary}")
print(f"Your monthly in-hand salary: {monthly_in_hand}")
