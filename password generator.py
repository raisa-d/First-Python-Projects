import random
import string

def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(all_chars) for i in range(length))
    return password

password = generate_password(12)
print("Your new password is", password)