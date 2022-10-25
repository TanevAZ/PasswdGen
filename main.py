import random
import string

def password_generator():
    length = int(input("How many characters : "))
    nbOfPaswd = int(input("How many passwords : "))
    spchars = input("Would you like special characters (y/n) : ")
    numbers = input("Would you like numbers (y/n) : ")
    uppercase = input("Would you like uppercase letters (y/n) : ")
    lowercase = input("Would you like lowercase letters (y/n) : ")


    for i in range(nbOfPaswd):
        password = ""
        for i in range(length):
            if spchars == "y":
                password += random.choice(string.punctuation)
            if numbers == "y":
                password += random.choice(string.digits)
            if uppercase == "y":
                password += random.choice(string.ascii_uppercase)
            if lowercase == "y":
                password += random.choice(string.ascii_lowercase)

        print(password)

    with open("passwords.txt", "a") as file:
        file.write(password + " ")

password_generator()