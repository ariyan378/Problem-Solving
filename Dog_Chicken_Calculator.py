heads = int(input("Enter total number of heads: "))
legs = int(input("Enter total number of legs: "))

dogs = (legs - 2 * heads) // 2
chickens = heads - dogs

print(f"\nNumber of dogs: {dogs}")
print(f"Number of chickens: {chickens}")