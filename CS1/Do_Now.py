def difference(num1, num2):
    print(num2 - num1)

def is_positive(number):
    #return number.isnumeric()
    if number.isnumberic():
        return True
    else:
        return False

def main():
    difference(3, 5)
    number = input("Enter integer: ")
    print(is_positive(number))
    is_positive("3")
    is_positive(str(3))
main()
