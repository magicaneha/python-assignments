


class Exceptions(Exception):  ##inherit from base class Exception


       display_error = "Exception raised because '#' found."


def get_name():
    print("Please enter a name (if it contains a '#', an error message will appear): ")
    input = raw_input()  ####taking the input
    if input.find('#') == -1:
        return (input)  ## checking the required conditions
    else:
        raise Exceptions()


# EXECUTION
def fun_exception_handling():
    try:  ###Tries get_name().
        print(get_name())  ##Prints returned name_input.
    except Exceptions:
        print(Exceptions.display_error)  ###Displays exception text.


fun_exception_handling()  # Simply calls function.