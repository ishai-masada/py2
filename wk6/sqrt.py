import math

def newton(num):
    # Check if the number can be converted into a float
    try:
        num = float(num)
        if num < 0:
            print("You can only enter positive numbers")
            return False
    except:
        print("You can only enter numbers")
        return False

    # Set the tolerance to a small decimal value to increase the accuracy of the calculations
    tolerance = 0.000001

    # Start the calculations with an estimate value 1.0
    estimate = 1.0

    while True:
        # Redefine the estimate value using an unchanging caluclation
        estimate = (estimate + num/estimate) / 2

        # Check if the difference between the number and the estimate is within tolerance
        if abs(num - estimate**2) < tolerance:
            num = estimate
            break

    return num

def main():
    # Get a number value from the user
    num = input("Type in a positive number or nothing to end the program: ")

    # Conditional loop if the number value is not equal to an empty string
    while num != '':
        # Calculate the square root of the number using the newton function
        newton_root = newton(num)

        # Check if the function returns anything but False
        if newton_root:
            # Calculate the square root of the number using python's square root function
            python_root = math.sqrt(float(num))

            # Print out python's result and the newton function result
            print(f'The program\'s estimate is: {newton_root}')
            print(f'Python\'s built in function gives: {python_root}')

            # Calculate the discrepancy between the newton function and the python
            # square root function
            discrepency = abs(newton_root - python_root)

            # Print out the discrepancy
            print(f'The program\'s answer was off by: {discrepency}')

        # Prompt the user for another number
        num = input("\nType in a positive number or nothing to end the program: ")

main()
