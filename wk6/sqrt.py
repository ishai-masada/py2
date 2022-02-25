import math

def newton(num):
    try:
        num = float(num)
        if num < 0:
            print("You can only enter positive numbers")
            return False
    except:
        print("You can only enter numbers")
        return False
    tolerance = 0.000001
    estimate = 1.0
    while True:
        estimate = (estimate + num/estimate) / 2
        if abs(num - estimate**2) < tolerance:
            num = estimate
            break
    return num

def main():
    num = input("Type in a positive number or nothing to end the program: ")
    while num != '':
        newton_root = newton(num)
        if newton_root:
            python_root = math.sqrt(float(num))
            print(f'The program\'s estimate is: {newton_root}')
            print(f'Python\'s built in function gives: {python_root}')
            discrepency = abs(newton_root - python_root)
            print(f'The program\'s answer was off by: {discrepency}')
        num = input("\nType in a positive number or nothing to end the program: ")

main()
