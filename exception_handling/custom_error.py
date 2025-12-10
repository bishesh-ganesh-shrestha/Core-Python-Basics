class CustomError(Exception):
    def __init__(self, error_message):
        self.error_message = error_message

def enter_number(number):
    try:
        if not isinstance(number, (int, float)):
            raise CustomError(f"{number} is not a number")
        print("Number entered is:", number)
    except CustomError as e:
        # print (type(e))
        # print(e)
        print('Error:', e.error_message)
    # finally:
    #     print("Execution completed.")
        
enter_number(123)
enter_number('abc')