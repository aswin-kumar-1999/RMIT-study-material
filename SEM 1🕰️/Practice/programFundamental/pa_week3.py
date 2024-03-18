#QUESTION 1

val=10
val*=2
print(val)

val+=100
print(val)

val=val/4
val%=7
print(val)


#QUESTION 2
print("She\'s the daughter of \"Treeman\"!!\n")
print("#"*40,"\n")
print("Hello there. \nI'm learning to code. \n")
a=3
b=5
print("a is",a,", b is",b,", a x b is",a*b)

#QUESTION 3
str1="Hello"
print(str1.lower())
str2="S1234567"
starts_with_S=str2.startswith("S")
print(starts_with_S)
str3="123"
is_numeric=str3.isnumeric()
print(is_numeric)

#QUESTION 4
list=["Harry","Hermione","Ron","Dumbledore","Hagrid"]
print(list[0])
print(list[-1])
print(list[2],list[3])
print(list[1],list[-1])

#QUESTION 5
number = 5
if number > 0:
    print ("I see a positive number!")

#QUESTION 6
exam_result = 90
is_cheat = True

if exam_result >= 50 and not(is_cheat):
    print("PASS")

if exam_result < 50 or is_cheat:
    print("FAIL")


#QUESTION 7
school_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

is_lockdown = False
today = 'Monday'

if school_days.__contains__(today) and not(is_lockdown):
    print("I am going to RMIT.")
elif school_days.__contains__(today) and is_lockdown:
    print("I am studying from home.")
elif not(school_days.__contains__(today)) and not(is_lockdown):
    print("I am going to the Brighton beach.")
else :
    print("I am staying at home")

# QUESTION 8
userInput=int(input("Enter a number"))
print(userInput)
if userInput > 0:
    print("Positive")
elif userInput == 0:
    print("Zero")
else:
    print("Negative")

#QUESTION 9
product_list = ["desk", "chair", "bed", "drawer"]
product_sale_list = ["desk", "drawer"]
userInput=str(input("product name")).strip().lower()
print(userInput)
if product_list.__contains__(userInput):
    print("This is an existing product.")
    if(product_sale_list.__contains__(userInput)):
        print("Alert! This product is on sale!")
else:
    print("This is not an exisiting product.")

# QUESTION 10
count=0
while(count<20):
    count+=1
    print(count)