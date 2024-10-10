import hashlib
import random
import string

def generate_password(str1, str2):
    passwordChars={}
    combined_str = str1 + str2
    
    hashed = hashlib.sha256(combined_str.encode()).hexdigest()
    
    password = hashed[:8]
    
    if (not any(c.isupper() for c in password) or
        not any(c.islower() for c in password) or
        not any(c.isdigit() for c in password) or
        not any(c in string.punctuation for c in password)):

        all_chars = string.ascii_letters + string.digits + string.punctuation

        for _ in range(8):
            random_char = random.choice(all_chars)
            passwordChars.append(random_char)
        password = ''.join(passwordChars)

    return password

if __name__ == "__main__":
    str1 = "Texto1"
    str2 = "Texto2"
    password = generate_password(str1, str2)
    print(password)
