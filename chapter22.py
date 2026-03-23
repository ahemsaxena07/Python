#exceptional handling
try:
    a = int(input('enter a no.: '))
    b = int(input('enter a no.: '))
    c = a / b
    print('c =', c)

except ZeroDivisionError as zde:
    print("denominator is 0")
    print(zde.args)
    print(zde)

except ValueError:
    print('Unable to convert string to int')

except:
    print('some unknown error')
