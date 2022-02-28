from turtle import up


i = 0
numbers = []
j = int(input("range: "))
up = int(input("incremental change: "))

while i < (j):
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + up
    print("Numbers now: ",numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)