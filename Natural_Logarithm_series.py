# Natural Logarithm Series Approximation
# Calculate the sum of the first 7 terms of the series

x = float(input("Enter the value of x: "))

# Initialize sum
series_sum = 0

# Calculate the sum of first 7 terms
for n in range(1, 8):
    # Calculate (x-1)/x
    base = (x - 1) / x
    # Calculate the nth term: (1/n) * base^n
    term = (1 / 2) * (base ** n)
    series_sum += term

print(f"The sum of the series till the 7th term is: {series_sum}")