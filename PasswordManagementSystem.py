from FileController import FileController
from Utils import validateIntSize
from MasterPasswordManager import *
from PasswordManager import *


if __name__ == "__main__":
    file_controller = FileController('mpwd.txt')
    
    master_password = changeMasterPassword(file_controller)

    user_str = input("Veuillez entrer une chaîne de caractères: ")
    #size = validateIntSize(0, 1, 12)
    size=1
    
    password = generatePassword(master_password, user_str, size)
    print("Mot de passe généré: ", password)
    

    file_controller = FileController('mpwd.txt')
    
    master_password = getMasterPassword(file_controller)

    real_passwords = {
        "Unilim": generatePassword(master_password, "Unilim", 1),
        "Amazon": generatePassword(master_password, "Amazon", 1),
        "Netflix": generatePassword(master_password, "Netflix", 1)
    }
    
    print("Tentando encontrar o mot de passe maître via ataque de dicionário...")
    brute_force_attack(real_passwords, 10)
    
