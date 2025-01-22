''' class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed"):
        self.message = message
        super().__init__(self.message)

    def check_positive_number(number):
        if number < 0:
            raise NegativeNumberError(f"The number provided is negative: ".format(number))
        else:
            return " The number is positive : {}".format(number)
        
        
        
def main():
    try:
        number = float(input("enter a number:"))
        result = check_positive_number(number)
        print(result)
    except NegativeNumberError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        
  """      return f'self.value} -> {self.message}'

    def check_positive_number(number):
        if number < 0:
            raise NegativeValueErrror(number)
        return number ** 0.5

     #   else:
      #      return "The number is positive :{}".format(number)


# def main():
#    try:
     #   num = float(input("enter a number:"))
    #    result = check_positive_number(num)
   # except NegativeValueError as e:
  #      print(f'Error:{e}')
 #   except ValueError:
     #   print('Invalid input. please enter a valid number.')
    #else:
   #     print(f'The square root of  {num} is {result}.')
  #  finally:
 #       print('Execution of square root complete.')"""


if __name__ == "__main__":
    main()
'''
class NegativeNumberError(Exception):
    '''Exception raised for errors in the input if the number is negative.'''
    
    def __init__(self, value):
        self.value = value
        self.message = f'Invalid input : {value}. Number must be non-negative.'
        super().__init__(self.message)
        
def square_root(number):
    if number < 0:
        raise NegativeNumberError(number)
    return number ** 0.5

def main():
    try:
        num = float(input('Enter a number to find its square root:'))
        result = square_root(num)
        print(f'The square root of {num} is {result}')
    except NegativeNumberError as e:
        print(e)
    except ValueError:
        print('Invalid input! Please enter a valid number.')
        
        
        
if __name__ == "__main__":
    main()