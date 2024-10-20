from FileController import *


def validatePassword(master_password):
    if ' ' in master_password:
        print("Le mot de passe maître ne peut pas contenir d'espaces.")
        return False
    return True

def getMasterPassword(file_controller):
    if file_controller.isEmpty():
        while True:
            master_password = input("Veuillez entrer un nouveau mot de passe maître (pas d'espaces): ")
            if validatePassword(master_password):
                file_controller.write_to_file(master_password, mode='w')
                return master_password
    else:
        return file_controller.read_from_file().strip()

def changeMasterPassword(file_controller):
    changeChoice = input("Voulez-vous changer le mot de passe maître ? (y/n): ")
    if changeChoice == 'y':
        while True:
            new_password = input("Veuillez entrer un nouveau mot de passe maître : ")
            if validatePassword(new_password):
                file_controller.write_to_file(new_password, mode='w')
                print("Le mot de passe maître a été changé.")
                return new_password
    else:
        return getMasterPassword(file_controller)
