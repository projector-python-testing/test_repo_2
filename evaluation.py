def evaluate(a: int, b: int, c: int) -> int:
    result = None
   
    #try:
    a = int(a)
    b = int(b)
    if c == "add":
        result = a + b
    elif c == "divide":
        result = a / b
    return result

    #add error of dividing by 0


#test_change



def add_numbers(a: int, b:int) -> int:
    return a+b

def multiply_numbers(a: int, b:int) -> int:
    return a/b

def divide_numbers(a: int, b:int) -> int:
    return a/b