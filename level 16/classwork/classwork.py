# 1) შექმენით for loop'ი რომელიც 0'დან 200'მდე დაპრინტავს ყოველ მეექვსე რიცხვს

for i in range(0, 200, 6): 
    print(i)

# 2) გადაატეთ for loop'ი სტრინგს: "Goodbye World!"

str1 = "Goodbye World!"


for i in str1:
    print("Goodbye World!")

# 3) შექმენით for loop'ი რომელიც 1000'დან 0'მდე დაპრინტავს ყველა რიცხვს

for i in range (1000, 0, -1):
    print(i)

# 4) მაღაზიაში არის ფასდაკლება მხოლოდ არასრულწოვნებზე. არასრუწლოვანი ადამიანი მიიღებს 50%იან ფასდაკლებას ხოლო სრულწლოვანი გადაიხდის ჩვეულებრივ ფასს. დაწერე პროგრამა რომელიც ადამიანს ეტყვის მან მიიღო თუ არა ფასდაკლება.

age = int(input("Enter your age:"))

if age >= 18:
    print("you didn't get dicount")
else:
    print("You got 50%'  discount. ")


# 5) მაღაზიაში არის ფასდაკლება მხოლოდ არასრულწოვნებზე და 18 წლის ხალხზე. არასრუწლოვანი ადამიანი მიიღებს 50%იან ფასდაკლებას, 18 წლის ადამიანი მიიღებს 25% ფასდაკლებას, ხოლო სრულწლოვანი გადაიხდის ჩვეულებრივ ფასს. დაწერე პროგრამა რომელიც ადამიანს ეტყვის მან მიიღო თუ არა ფასდაკლება და თუ მიიღო რამდენი.

if age >18: 
    print("you didn't get disscount")
elif age == 18:
    print("you got 25%' disscount.")
else:
    print("you got 50%' disscount.")


# 6) მაღაზიაში ფასდაკლება არის მხოლოდ არასრულწოვნებზე და სტუდენტებზე. არასრუწლოვანი ან სტუდენტი ადამიანი მიიღებს 50%იან ფასდაკლებას ხოლო სრულწლოვანი ან არასტუდენტი გადაიხდის ჩვეულებრივ ფასს. დაწერე პროგრამა 
# რომელიც ადამიანს ეტყვის მან მიიღო თუ არა ფასდაკლება.

age = int(input("Enter your age: "))
is_student = False
if age <18 or is_student:
    print("you got 50%' discount.")
else:
    print("Regular price.")