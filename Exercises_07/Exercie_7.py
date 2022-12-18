def divide_two_numbers():

    try:
        a= input("Enter Fuel in litres: ")
        b= input("Enter fuel consumption - in litres per minute: ")

        c= int(float(a)) / int(float(b))
    
    except ZeroDivisionError:
        c="You cannot divide by Zero."

    print ((c), "Minutes")

divide_two_numbers()