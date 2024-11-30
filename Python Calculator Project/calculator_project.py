import sys
from art import logo


def addition(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def calculator():
    should_accumulate = True
    operations = {"+": addition,
                  "-": subtract,
                  "*": multiply,
                  "/": divide}

    calc_num1 = int( input( "What is the first number? : " ) )
    while should_accumulate:
        for symbol in operations:
            print( symbol )

        operation_symbal = input( "Pick an operation : " )
        calc_num2 = int( input( "What is the next number? : " ) )
        # addition(num1=calc_num1, num2=calc_num2)

        calc_result = operations[operation_symbal]( num1=calc_num1, num2=calc_num2 )
        print( f"{calc_num1} {operation_symbal} {calc_num2} = {calc_result}" )
        command = input(
            f"Type 'y' to continue with {calc_result}, or type 'n' to start a new calculation, or 'e' for exit the calculator: \n" ).lower()

        if command == 'y':
            calc_num1 = calc_result
        elif command == 'n':
            should_accumulate = False
            print( "\n" * 20 )
            calculator()
        elif command == 'e':
            print( "Exiting the program..." )
            sys.exit( 0 )
        else:
            print( "You entered incorrect value." )
            print( "Calculator program starts again." )
            print( "\n" * 20 )
            calculator()


if __name__ == "__main__":
    print( "WELCOME TO PYTHON CALCULATOR! " )
    print( logo )
    calculator()
