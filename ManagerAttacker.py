import string
from MasterPasswordManager import *
from PasswordManager import *


def numberOfCombinations(size):
    
    for i in range(size-1):
        numberOfCombinations=numberOfCombinations*size
    return numberOfCombinations

def generateCombinations(size):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    if size == 0:
        return ['']
    
    smaller_combinations = generateCombinations(size - 1)
    combinations = []
    
    for combo in smaller_combinations:
        for char in all_chars:
            combinations.append(combo + char)
    
    return combinations

def bruteForceAttack(real_passwords, size=10):
    all_combinations = generateCombinations(size)
    attempts = 0
    
    for candidate in all_combinations:
        attempts += 1
        candidate_unilim = generatePassword(candidate, "Unilim", 1)
        candidate_amazon = generatePassword(candidate, "Amazon", 1)
        candidate_netflix = generatePassword(candidate, "Netflix", 1)
        
        if (candidate_unilim == real_passwords["Unilim"] and
            candidate_amazon == real_passwords["Amazon"] and
            candidate_netflix == real_passwords["Netflix"]):
            print(f"Mot de passe maitre trouvée: {candidate}")
            print(f"Nombre d'essaies: {attempts}")
            return candidate

    print("Pas de mot de passe (collision) trouvée.")
    return None

if __name__ == '__main__':
    
    combinations=generateCombinations(3)
    for combo in combinations:
        print(combo)
