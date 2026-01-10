def power(a, b):
    if b == 0:
        return 1
    if a != 0:
        return a * power(a, b - 1) #thats the fucking maths
    else:
        return 0
number = int(input('enter a number: '))
powers = int(input('enter a power: '))
final = power(number, powers)
print(f"the answer is: {final}")