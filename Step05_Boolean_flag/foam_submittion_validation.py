# FOR Now we don't have any foam that way we add three input to check it's work or not .
name=input("Enter your Name : ")
email=input("Enter your Email : ")
age=int(input("Enter your Age : "))

# this check-in professional foam to check user fill all the foam .
is_form_valid = True

if name == "":
    is_form_valid = False
if email == "":
    is_form_valid = False
if not age.isdigit():
    is_form_valid = False

if is_form_valid:
    print("Form submitted successfully!")
else:
    print("Please fill out all fields correctly.")
