'''
Gets an operand and ensures the input is of float type.

@return The inputted operand
'''
def get_operand():
    while True:
        try:
            operand = float(input("Enter an operand: "))
            break
        except:
            print("Invalid operand")
    return operand

def main():
    print("Calculator")
    while True:
        operator = str(input("\nEnter an operator (+ - * /) or q to quit: "))
        valid_operators = ['+', '-', '*', '/', 'q']
        while operator not in valid_operators:
            operator = str(input("Invalid operator. Try again: "))

        if operator == 'q':
            break

        operand1 = get_operand()
        operand2 = get_operand()

        match operator:
            case '+':
                print("Result: %g" %(operand1 + operand2))
            case '-':
                print("Result: %g" %(operand1 - operand2))
            case '*':
                print("Result: %g" %(operand1 * operand2))
            case '/':
                while operand2 == 0: # no division by 0
                    try:
                        operand2 = float(input("Enter the second operand: "))
                    except:
                        print("Invalid operand, cannot divide by 0")
                print("Result: %g" %(operand1 / operand2))

if __name__ == "__main__":
    main()