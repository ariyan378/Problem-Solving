s = input('Enter your string :')

words = s.split()
reverse = words[::-1]
output_string = ' '.join(reverse)
print(f"Your reverse string is {output_string}")
