# What is Boolean flag , boolean flag is assume a suition and taking decision on it .
password=input("Set a password : ")

is_strong= True
special_character="!@#$%^&*()"
print("\n")
if len(password) < 8:
    is_strong= False
if not any(character.isupper() for character in password):
    is_strong=False
    print("Enter a Uppercase .")
if not any(character.isdigit() for character in password):
    is_strong=False
    print("Enter a Digit .")
if not any(character in special_character for character in password):
    is_strong=False
    print("Plz enter a special character.")

if is_strong:
    print("Wow! The Password is Strong .")
else:
    print("Weak Password , Enter a strong password")
