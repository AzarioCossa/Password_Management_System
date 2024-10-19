from FileController import FileController
from Utils import validateIntSize
from MasterPasswordManager import *
from PasswordManager import *
from ManagerAttacker import *


if __name__ == "__main__":
    
    fileController = FileController('mpwd.txt')
        
    masterPassword = changeMasterPassword(fileController)

    #user_str = input("Veuillez entrer une chaîne de caractères: ")
    #size = validateIntSize(0, 1, 12)

    real_passwords = {
        "Unilim": generatePassword(masterPassword, "Unilim", 1),
        "Amazon": generatePassword(masterPassword, "Amazon", 1),
        "Netflix": generatePassword(masterPassword, "Netflix", 1)
    }
    
    print("Tentatives de trouver le mot de passe maitre via attaque par dictionnaire.")
    for i in range(1, 4):
        print("Collisions de taille : ", i)
        bruteForceAttack(real_passwords, i)
    
