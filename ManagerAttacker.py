import string
import itertools
from MasterPasswordManager import *
from PasswordManager import *


def numberOfCombinations(size):
    
    for i in range(size-1):
        numberOfCombinations=numberOfCombinations*size
    return numberOfCombinations

def generateCombinations(size):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    combinations = [''.join(combo) for combo in itertools.product(all_chars, repeat=size)]
    return combinations

def bruteForceAttack(real_passwords, size):
    all_combinations = generateCombinations(10)
    attempts = 0
    collisions = []
    
    for candidate in all_combinations:
        attempts += 1
        candidate_unilim = generatePassword(candidate, "Unilim", size)
        candidate_amazon = generatePassword(candidate, "Amazon", size)
        candidate_netflix = generatePassword(candidate, "Netflix", size)
        
        if (candidate_unilim == real_passwords["Unilim"] and
            candidate_amazon == real_passwords["Amazon"] and
            candidate_netflix == real_passwords["Netflix"]):
            print(f"Collision du mot de passe maitre trouvée: {candidate}")
            print(f"Nombre d'essaies: {attempts}")
            collisions.append(candidate)
        
    if len(collisions)==0:
        print("Pas de mot de passe (collision) trouvée.")
        return None
    else:
        return collisions



def bruteForceAttackForTag(real_password, tag, size=10):
    all_chars = string.ascii_letters + string.digits+string.punctuation
    attempts = 0
    
    for candidate in itertools.product(all_chars, repeat=size):
        candidate_password = ''.join(candidate)
        attempts += 1
        
        candidate_hash = generatePassword(candidate_password, tag, 3)
        if candidate_hash == real_password:
            print(f"Mot de passe maître trouvé: {candidate_password}")
            print(f"Nombre de tentatives: {attempts}")
            return candidate_password

    print("Aucun mot de passe maître correspondant trouvé.")
    return None