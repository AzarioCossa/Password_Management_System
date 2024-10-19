import string


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

if __name__ == '__main__':
    
    combinations=generateCombinations(3)
    for combo in combinations:
        print(combo)