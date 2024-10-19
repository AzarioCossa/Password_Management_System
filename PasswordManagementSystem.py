from FileController import FileController
from Utils import validateIntSize
from MasterPasswordManager import *
from PasswordManager import *
from ManagerAttacker import *


if __name__ == "__main__":
    
    fileController = FileController('mpwd.txt')
        
    masterPassword = changeMasterPassword(fileController)

    #user_str = input("Veuillez entrer une chaîne de caractères: ")
    
    
    #size = validateIntSize(1, 1, 12)

    size=3
    
    real_passwords = {
        "Unilim": generatePassword(masterPassword, "Unilim", size),
        "Amazon": generatePassword(masterPassword, "Amazon", size),
        "Netflix": generatePassword(masterPassword, "Netflix", size)
    }
    
    for tag in real_passwords:
        print("Mot de passe pour", tag + ":", real_passwords[tag])
        print("Double verif", tag, "  ", generatePassword(masterPassword, tag, size))
    
    print("Tentatives de trouver le mot de passe maitre via attaque par dictionnaire.")
    bruteForceAttackForTag(real_passwords, "Unilim", size=3)
    #bruteForceAttack(real_passwords, 2)
    
    