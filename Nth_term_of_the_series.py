# Take inputs from the user
a1 = int(input("Enter the first term (a1): "))
a2 = int(input("Enter the second term (a2): "))
n = int(input("Enter the term number (n): "))

# Common difference
d = a2 - a1

# Nth term formula: a_n = a1 + (n - 1) * d
nth_term = a1 + (n - 1) * d

# Output the result
print(f"\nThe {n}th term of the series is: {nth_term}")