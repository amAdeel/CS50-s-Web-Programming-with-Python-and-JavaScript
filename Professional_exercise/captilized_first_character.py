# we have list of selected candidate in piaic course .


student_names = [
    "Ayesha Khan",
    "Ali Ahmed",
    "Riya Sharma",
    "Arjun Singh",
    "Sara Malik",
    "Rahul Verma",
    "Zara Ali",
    "Hassan Raza",
    "Meena Patel",
    "Adil Sheikh",
    "Fatima Tariq",
    "Kabir Hussain",
    "Sana Mir",
    "Ishaan Kumar",
    "Zainab Iqbal",
    "Rohan Gupta",
    "Nida Anwar",
    "Aman Gill",
    "Mahnoor Zafar",
    "Imran Siddiqui",
    "Adeel Ashraf"
]

find_your_name=input("Your Full Name : ")
#step01 convert string into a list 
splite_string=find_your_name.split()
captilized_list=[]
# step02 applying for loop for access each words separately 
for i in splite_string:
    first_character=i[0].capitalize()
    second_charcter=i[1:].lower()
    final_captilized_character= first_character + second_charcter
    # here we get both word separatley with first word capital . now we create a empty string where a append each other one by one .
    captilized_list.append(final_captilized_character)

# here we get a list of word with first word capital and other is small .
## now it's time to reconvert this list into a singal string 

joined_string=" ".join(captilized_list)

if joined_string in student_names:
    print(f"Congraturation {joined_string} ! your are selected for Desire course . Best of Luck")
else:
    print(f"Sorry {joined_string} ! Better luck for Next time .")

