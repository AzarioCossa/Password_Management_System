import string
from FileController import FileController
from Utils import validateIntSize
from MasterPasswordManager import *
from PasswordManager import *
from ManagerAttacker import *


if __name__ == "__main__":
    """
    DISCLAIMER
    Tout le code commenté dans les fichiers, est utile pour les exerccices
    Il est seulement commenté pour automatiseer les tests
    """
    
    fileController = FileController('mpwd.txt')
        
    masterPassword = changeMasterPassword(fileController)

    #user_str = input("Veuillez entrer une chaîne de caractères: ")
    #size = validateIntSize(1, 1, 12)

    size=1
    
    realPasswords = {
        "Unilim": generatePassword(masterPassword, "Unilim", size),
        "Amazon": generatePassword(masterPassword, "Amazon", size),
        "Netflix": generatePassword(masterPassword, "Netflix", size)
    }
    
    realPassword=realPasswords["Unilim"]
    
    print("Tentatives de trouver le mot de passe maitre via attaque par brute force.")
    #print("Generated Passwords:", realPassword)
    bruteForceAttackOnTag(realPassword, "Unilim", size)
    #bruteForceAttack(real_passwords, size)
    
