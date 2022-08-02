print('input the maximum number in the list')
number = int(input())
counter = 0
while number >1:
    number = number / 2
    counter += 1
print(f"The maximum number of tries is {counter}")