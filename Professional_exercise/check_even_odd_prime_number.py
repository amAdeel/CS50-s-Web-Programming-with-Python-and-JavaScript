import random


num=int(input("Enter a Number : ")) # input always return a string value that why i firstly convert in int .

def checkeven():
    if num % 2 ==0 :
        print(f"Number is Even : {num}\n")
    elif num%2 ==1:
        print(f'Number is Odd : {num}\n')
checkeven()      




### profession exercise
## first we genrate a list of random number ,import random and use random.randint(min_num,Max_num)yaha hum ny range set ki hai k kaha sy ly kr kaha tak is ki range hai or phir hum ny for loop k sath hum ny ak range dy di matlab k har bar hum ko 10 number in list print kar k do .

my_count=10
min_num=1
max_num=100
random_number=[random.randint(min_num,max_num) for _ in range(my_count)]
even_number=[]
odd_number=[]

#===================> check even or odd number <=======================================


for number in random_number:
    if number%2 ==0:
        even_number.append(number)
    elif number%2 ==1:
        odd_number.append(number)
print(f"Random Number : {random_number}")
print(f"Even Number in List : {even_number}")
print(f"Odd Number in List : {odd_number}")







#========================> check prime number <==========================

prime_number=[]
not_prime_number=[]


for number in random_number:
 if number <=1:
  not_prime_number.append(number)
 else:
  is_prime=True
  for i in range(2,number):
   if number%i ==0:
    is_prime=False
    break
 if is_prime:
  prime_number.append(number)
 else:
  not_prime_number.append(number)

  

print(f"Prime Number in List : {prime_number}")
print(f"Not the Prime Number in List : {not_prime_number}\n")


# m ny sb sy phele 2 empty list bany or os k bad ak for loop chalaya jo random number ko aleda aleda kar raha hai . os k bad m ny loop k under hi pheli if condition lagi like os me check kiya k agr to number jo hai wo agr 1 k barber ya chota hai to wo to prime number nahi ho sakta to loop yahi pr khatam ho jy ga ,or agr ya condition false aye gi to wo else py jaye ga jaha pr m ny ak boolen flag diya hai ,jo m assume kar raha ho k true hai ,"is_prime=True" or is else k under m ny loop chalaya jo check kary ga k prime number hai k nahi , for i in range(2,number) is ko range m ny starting point two or endingpoint before number dy diya matlab k number sy phele ya loop end ho jy ga , nijy hum ny number ko divide kar diya i sy agr to wo completely divide ho gy to matlab ya prime number nahi hai or hum ny loop ko yaha pr break kiya . or then hum main loop k under ak if or ak else lagya jo jaha hum ny number empty list ko forward karva diya if assume kary ga k number is prime or wo number empty list me bj dy ga ,, or else pr agar loop aya to matlab wo prime number nahi hai to wo prime number nahi ta , or 2no list ko hum ny loop sy bhar print karva diya .


