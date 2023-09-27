numbers = []

for i in range(10):
    num = int(input("Введите число: "))
    numbers.append(num)

for number in numbers:
    if number % 2 == 0:
        print(number)
    if number == 237:
        break