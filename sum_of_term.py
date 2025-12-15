# Code here

n = int(input('Enter your Number :'))

total_sum = 0
current_term = 2
output_str = ""

for i in range(n):
    total_sum += current_term
    output_str += str(current_term)
    if i < n - 1:
        output_str += "+"
    current_term = current_term * 10 + 2

print(output_str)
print(f"Sum of above series is: {total_sum}")