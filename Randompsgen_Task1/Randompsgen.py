import random
import string

def passgen(length):
    characters = string.ascii_letters + string.digits + string.punctuation #Combines the password requirements including alphabets and special characters
    password = ''.join(random.choice(characters)for _ in range(length)) #Randomly combines all the characters in the desired length
    return password #Returns the password

def main():
    try:
        numberofpass = int(input("Enter number of passwords you want to generate : ")) #userinput of number of passwords
        pass_len = int(input("Enter the length of each password you want to generate : ")) #userinput of length of each password
    except ValueError:
        print("Please enter valid numberic values.") #Error message
    
    if numberofpass <=0 or pass_len<=0:
        print("Both the number of passwords required and password length of each password should be greater than 0....")
        return
    
    password = [passgen(pass_len)for _ in range(numberofpass)]
    
    for i,password in enumerate(password,1):
        print(f"Password {i} : {password}")
        

if __name__ == "__main__":
    main()
        