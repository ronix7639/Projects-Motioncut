def ctf(c): #converts celsius to fahrenheit
    f = (c*9/5)+32 #logic used for conversion
    return f

def ftc(f): #converts fahrenheit to celsius 
    c = (f- 32) * 5/9 #logic used for conversion
    return c

while True:
    print("Choose an option:")
    print("1. Convert from Celsius to Fahrenheit")
    print("2. Convert from Fahrenheit to Celsius")
    print("3. Quit")
    userchoice = input("Enter your userchoice (1,2,3): ") 
    if userchoice == '1':
        c = float(input("Enter temperature in Celsius to convert : "))
        f = ctf(c)
        print(f"{c}°C is approximately equal to {round(f)}°F") # returns celsius to fahrenheit
    elif userchoice == '2':
        f = float(input("Enter temperature in Fahrenheit to convert : ")) 
        c = ftc(f)
        print(f"{f}°F is approximately equal to {round(c)}°C") # returns fahrenheit to celsius
    elif userchoice == '3':
        print("Exiting .....!") #exit case
        break
    else:
        print("Invalid choice !! Please select a valid option  (1,2,3).") #Error case
