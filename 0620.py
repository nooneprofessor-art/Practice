try:
    num1, num2 = int(input()), int(input())
    num1 / num2
except ZeroDivisionError:
    print("Невозможно делить на ноль")
else:
    print("сука")