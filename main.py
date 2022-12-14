import random
import string
import platform
import os
from colorama import Fore

pm = platform.system()
if pm == "Windows":
    os.system("cls")
elif pm == "Linux":
    os.system("clear")
elif pm == "Darwin":
    os.system("clear")
banner = Fore.RED + f"""
                        ______                          _ _____            
                        | ___ \                        | |  __ \           
                        | |_/ /_ _ ___ _____      ____ | | |  \/ ___ _ __  
                        |  __/ _` / __/ __ \ \ /\ / / _` | | __ / _ \ '_ \ 
                        | | | (_| \__ \__ \ \ V  V / (_| | |_\ \  __/ | | |
                        \_|  \__,_|___/___/  \_/\_/ \__,_|\____/\___|_| |_|

                               Github : https://github.com/TanevAZ
"""

print(banner)

def PasswdGen():
    # password length
    passwdLength = int(input(f"{Fore.RESET}Enter the length of password : "))
    passwdCount = int(input("How many passwords do you want to generate : "))
    saveToFile = input("Do you want to save the passwords to a file (y/n) : ")
    passwdChars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase + string.digits
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
