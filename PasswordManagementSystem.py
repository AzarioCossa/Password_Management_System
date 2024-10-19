from FileController import FileController
from Utils import validateIntSize
from MasterPasswordManager import *
from PasswordManager import *


if __name__ == "__main__":
    file_controller = FileController('mpwd.txt')
    
    master_password = change_master_password(file_controller)

    user_str = input("Veuillez entrer une chaîne de caractères: ")
    #size = validateIntSize(0, 1, 12)
    size=1
    
    password = generate_password(master_password, user_str, size)
    print("Mot de passe généré: ", password)
    
