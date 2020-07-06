for value in range(1,5):
    print(value)
numbers = list(range(1,6))
print(numbers)

square = []
for value in range(1,11):
    square.append(value**2)
print(sum(square))
print(min(square))
print(max(square))
print(square)
#list comprehension
square_list = [value + 3 for value in range(1,11)]
print(square_list)

numlist = [digits + 0 for digits in range(1,1000000)]
print(numlist)
