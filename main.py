import random
import string
import os

def PasswdGen():
    passwdLength = int(input("Enter the length of password : "))
    passwdCount = int(input("How many passwords do you want to generate : "))
    saveToFile = input("Do you want to save the passwords to a file (y/n) : ")
    passwdChars = string.ascii_letters + string.digits + string.punctuation + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    password = []
    passwdList = []

    for x in range(0, passwdCount):
        for y in range(0, passwdLength):
            password.append(random.choice(passwdChars))
        passwdList.append(''.join(password))
        password = []

    for password in passwdList:
        print(password)

    if saveToFile == 'y':
        filename = input("Enter the file name : ")
        if filename == '':
            filename = "passwords.txt"
            print(f"Passwords saved to default file name : {filename}")
            
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        filePath = input(f"Enter the file path (default path : {desktop}\{filename} ) : ")
                         
        if filePath == '':
            filePath = os.path.join(os.path.expanduser('~'), 'Desktop', filename)
                         
            with open(filePath, 'w') as file:
                for password in passwdList:
                    file.write(password + ' ' + '\n')
        else:
            file = open(os.path.join(filePath, filename), "w")

            for password in passwdList:
                file.write(password + " " + '\n')
                         
        file.close()

        print("Passwords saved to file : " + filePath)
    else:
        print("Passwords not saved to file.")

    input("Press enter to exit.")
    exit()

PasswdGen()
