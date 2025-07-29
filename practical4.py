#Question 1
def grade_exam(score):

    match score:
        case score if 90 <= score <= 100:
            grade = "A"
        case score if 80 <= score <= 89:
            grade = "B"
        case score if 70 <= score <= 79:
            grade = "C"
        case score if 60 <= score <= 69:
            grade = "D"
        case score if score < 60:
            grade = "F"

    match grade:
        case  "A" | "F" :
            article = "an "
        case _:
            article ='a '

    print("You got " + article + grade + " for the test.")

score=(int(input("Enter a score: ")))
grade_exam(score)

#I - score
#P - grade_exam 
#O - grade



#Question 2 tung tung tung tung tung tung tung tung tung sahur omaygot ambatukod
import random

promptMessage = "Enter your guess as 1 for head, 2 for a tail, or 0 to exit: "
exitMessage = "Thank you for playing the game!"
correctMessage = "Your guess is correct!"
incorrectMessage = "Your guess is incorrect!"

while True:
	choice = int(input(promptMessage))
	if choice == 0:
		print(exitMessage)
		break
	else:
		message = correctMessage if random.randint(1, 2) == choice else incorrectMessage
		print(message)
	print("\n")

#Question 3
#-----------------------------------------
#I - working hour
#P - calculate total salary, regular pay and overtime pay
#O - total salary, regular pay and overtime pay

#CODE
hours = int(input("Enter hours: "))

hourly_rate = 40
OT_rate = hourly_rate * 1.5
extra_OT_rate = hourly_rate * 2
hourly_limit = 35
OT_limit = 25
regularpay = 0
overtimepay = 0

if hours <= hourly_limit:
    regularpay = hours * hourly_rate
    hours = 0
else:
    regularpay = hourly_limit * hourly_rate
    hours -= hourly_limit
if hours <= OT_limit:
    overtimepay = hours * OT_rate
    hours = 0
else:
    overtimepay = OT_limit * OT_rate
    hours -= OT_limit
overtimepay += hours * extra_OT_rate
total_salary = regularpay + overtimepay

print("Total:", total_salary)
print("Regular:",regularpay)
print("OT:",overtimepay)

#PSEUDOCODE
#START 
#   READ HOURS
#   Set hourly_rate = 40
#				OT_Rate = hourly_rate * 1.5
#				extra_OT_rate = hourly_rate * 2
#				hourly_limit = 35
#				OT_limit = 25
#       regularpay = 0
#       overtimepay = 0
#   IF hours <= hourly_limit
#   	regularpay = hours * hourly_rate
#     hours = 0
#   ELSE regularpay = hour_limit * hourly_rate, hours -= hour_limit
#   ENDIF
#   IF hours <= OT_limit
#   	overtimepay = hours * OT_rate
#     hours = 0
#   ELSE overtimepay = OT_limit * OT_rate, hours -= OT_limit
#   ENDIF
#   overtime_pay += hours * extra_OT_rate
#   total_salary = regularpay + overtimepay
#   output total_salary, regularpay and overtimepay
#END

# Question 4
#------------------------------------------------
# PSEUDOCODE
#START
#INPUT sales
#SET comm1 = 0.01
#    comm2 = 0.05
#    comm3 = 0.10
#    commission
#IF 1 <= sales <= 1000
#    commission = sales * comm1
#ELSE IF 1001 <= sales <= 10000
#    commission = sales * comm2
#ELSE
#    commission = sales * comm3
#OUTPUT commission
#END
#-------------------------------------------------
# CODE
sales = float(input("Enter sales value (RM): "))

if sales >= 1 and sales <= 1000:
    rate = 0.01
elif sales <= 10000:
    rate = 0.05	
elif sales <= 100000:
    rate = 0.10
else:
    rate = 0.0  

commission = sales * rate

print("Commission: RM{:.2f}".format(commission))


#Question 5
#PSEUDOCODE
#START
#    SET highest = -1
#    SET secondhighest = -1
#    SET total = 0
#INPUT numOfStudent
#	FOR i = 1 TO numOfStudents DO
#    Calculate suffix based on i
#    Input score of the i-th student
#    Add score to total

#    IF score > highest THEN
#        second_highest = highest
#        highest = score
#    ELSE IF score > second_highest THEN
#        second_highest = score
#    ENDIF
#END FOR

#Set average = total / numOfStudents

#Display "Highest score is" + highest + "%"
#Display "Second highest score is" + second_highest + "%"
#Display "Average score is" + average + "%"

#END
#---------------------------------------------------------
#CODE
def get_suffix(n):
    last_digit = n % 10
    match last_digit:
        case 1:
            return "st"
        case 2:
            return "nd"
        case 3:
            return "rd"
        case _:
            return "th"

num_students = int(input("Enter number of students: "))

highest = -1
second_highest = -1
total = 0

for i in range(1, num_students + 1):
    suffix = get_suffix(i)
    score = float(input(f"Enter score of the {i}{suffix} student: "))
    total += score

    if score > highest:
        second_highest = highest
        highest = score
    elif score > second_highest:
        second_highest = score

average = total / num_students

print("Highest score is", highest)
print("Second highest score is", second_highest)
print("Average score is", format(average, ".2f"))



#Question 6
positive_count = 0
negative_count = 0
total_sum = 0
total_count = 0

while (1):
    num = int(input("Enter a number: "))

    if num  == 0:
        break

    if num > 0:
        positive_count += 1
    else:
        negative_count += 1
    
    total_sum += num
    total_count += 1
    average = total_sum/total_count

print(f"No. of positive numbers: {positive_count}")
print(f"No. of negative numbers: {negative_count}")
print(f"Sum of all numbers: {total_sum}")
print(f"Average of all numbers: {average:.2f}")






#Question 7

#Pseudocode
#START
#   rate = 0.00417
#   total = 0.00
   
#   OUTPUT "Enter the monthly saving amount:"
#   INPUT salary

#   FOR i = 0 TO 5
#	interest = (salary + total) * (1 + rate)
#	total = interest
#   ENDFOR

#   OUTPUT "After the sixth month, the account value is RM"
#   OUTPUT total
#END

#Code
def main():

    salary = int(input("Enter the monthly saving amount : "))

    rate = 0.00417
    total = 0.00

    for num in range(0,6):
        interest = (salary + total)  * (1 + rate)
        total = interest

    print("After the six month, the account value is RM", round(total, 2))

main()

#Question 8

integer = int(input("Enter a positive integer: "))

print(chr(128073) + " Shape #1 " + chr(128072))
i = 1
while i <= integer:
    j = 1
    while j <= i: 
        print(j, end=" ")  
        j = j + 1 
    print()
    i = i + 1 

print()

print(chr(128073) + " Shape #2 " + chr(128072))
i = integer 
while i >= 1: 
    j = 1
    while j <= i: 
        print(j, end=" ")  
        j = j + 1 
    print()
    i = i - 1

print()

print(chr(128073) + " Shape #3 " + chr(128072))
i = 1
while i <= integer:
    s = integer - i
    while s > 0:
        print("  ", end="") 
        s = s - 1
    j = i
    while j >= 1:
        print(j, end=" ")
        j = j - 1
    print()
    i = i + 1

print()

print(chr(128073) + " Shape #4 " + chr(128072))
i = 1
while i <= integer:
    s = i - 1
    while s > 0:
        print("  ", end="")
        s = s - 1
    j = i
    while j <= integer:
        print(j, end=" ")
        j = j + 1
    print()
    i = i + 1


#Question 9

#Pseudocode
#START
#INPUT n
#FOR i = 1 TO n DO
#  total = 0
#   FOR j = 1 TO i DO
#      total = total + j
#      PRINT j
#      IF j < i THEN
#         PRINT " + "
#    END FOR
#  PRINT " = ", total
#END FOR
#END

#Code

n = int(input("Enter a positive integer: "))
for i in range(1, n + 1):
    total = 0
    for j in range(1, i + 1):
        total += j
        print(j, end='')
        if j < i:
            print(" + ", end='')
    print(" =", total)




#Question 10 - Create Quiz apps
QTY = 4
counter = 0

print("Let's start Quiz")

for i in range(QTY):
    print("-"* QTY*10)
    print("Q", i+1," : ", end=" ")

    #if match not support (python 3.9 and above), use to subtitute the match case with if i==0:
    
    match i:
        case 0:
            print("12 + 8 = ?")
            print("A. 14 \t B. 16\t C.18 \t D. 20")
            answer = input("\n Enter your answer (A or B or C or D) ")

            if answer == "D" or answer=="d":
                print("Correct!")
                counter+=1
            else :
                print("Wrong!")

        case 1:
            print("15 - 7 = ?")
            print("A. 6 \t B. 7\t C.8 \t D. 9")
            answer = input("\n Enter your answer (A or B or C or D) ")

            if answer == "C" or answer=="c":
                print("Correct!")
                counter+=1
            else :
                print("Wrong")

        case 2:
            print("9 x 6 = ?")
            print("A. 54 \t B. 45\t C.60 \t D. 48")
            answer = input("\n Enter your answer (A or B or C or D) ")

            if answer == "A" or answer=="a":
                print("Correct!")
                counter+=1
            else :
                print("wrong")

        case 3:
            print("40 / 5 = ?")
            print("A. 7 \t B. 9\t C.8 \t D. 10")
            answer = input("\n Enter your answer (A or B or C or D) ")

            if answer == "B" or answer=="b":
                print("Correct!")
                counter+=1
            else :
                print("Wrong")
    if i==QTY - 1:
        print("-"* 20)
    
if counter == 4:
    print("Conclusion: Congratulation, you got all correct!")
else:
    print("Conclusion: Keep practicing, and you'll improve!")
    

#Question 11 Rock Scissor paper game

import random
draw=0
win=0
lose=0
counter=0

while True:
    #0, 1, or 2 represent  "Scissor", "Rock" or "Paper"
    answer = random.randint(0,2)

    print("0 : scissor, 1 : rock, and 2: paper")
    while True:
        choice = int(input("Enter your choice : "))
        if choice==0 or choice == 1 or choice == 2:
            break
        else:
            print("Wrong input!")
    
    match answer:
        case 0:
            print("Computer choice is scissor")
        case 1:
            print("Computer choice is rock")
        case 2:
            print("Computer choice is paper")
    
    if choice== answer:
        print("Draw!")
        draw+=1
    elif (choice == 0 and answer == 2) or (choice == 1 and answer == 0) or (choice == 2 and answer == 1):
        print("You win!")
        win+=1
    else:
        print("You lose!")
        lose+=1
    
    counter+=1
    if (counter>2) and (win!=lose):
        print("you won",win," times" if win >1 else " times", end=" ")
        print("and computer ",lose," times" if lose >1 else " times")
        if win > lose:
            print("you are the winner!")
        else :
            print("Computer are the winner!")
        break

#question 12 
import random 

digit_1 = random.randint(0,9)
digit_2 = random.randint(0,9)
digit_3 = random.randint(0,9)

guess = input("Enter a 3 - digit integer : ")

guess_3 = guess % 10
answer = guess // 10
guess_2 = answer % 10
guess_1 = answer //10

if digit_1 == guess_1 and digit_2 == guess_3 and digit_3 == guess_3:
    print ("Congrats RM10,000")
elif(digit_1 and guess_1 and digit_2 == guess_3 and digit_3==guess_2) or \
    (digit_1 == guess_1 and digit_2 == guess_3 and digit_3==guess_3)or \
    (digit_1 == guess_2 and digit_2 == guess_1 and digit_3==guess_1)or \
    (digit_1 == guess_2 and digit_2 == guess_2 and digit_3==guess_1)or \
    (digit_1 == guess_3 and digit_2 == guess_1 and digit_3==guess_2):
    print ("Congrats RM3,000")
elif (digit_1 == guess_1 and digit_2 != guess_2 and digit_3 != guess_3) or \
     (digit_1 == guess_1 and digit_2 != guess_3 and digit_3 != guess_2) or \
     (digit_1 == guess_2 and digit_2 != guess_1 and digit_3 != guess_3) or \
     (digit_1 == guess_2 and digit_2 != guess_3 and digit_3 != guess_1) or \
     (digit_1 == guess_3 and digit_2 != guess_2 and digit_3 != guess_1) or \
     (digit_1 == guess_3 and digit_2 != guess_1 and digit_3 != guess_2) or \
     (digit_2 == guess_1 and digit_1 != guess_2 and digit_3 != guess_3) or \
     (digit_2 == guess_1 and digit_1 != guess_3 and digit_3 != guess_2) or \
     (digit_2 == guess_2 and digit_1 != guess_1 and digit_3 != guess_3) or \
     (digit_2 == guess_2 and digit_1 != guess_3 and digit_3 != guess_1) or \
     (digit_2 == guess_3 and digit_1 != guess_2 and digit_3 != guess_1) or \
     (digit_2 == guess_3 and digit_1 != guess_1 and digit_3 != guess_2) or \
     (digit_3 == guess_1 and digit_2 != guess_2 and digit_1 != guess_3) or \
     (digit_3 == guess_1 and digit_2 != guess_3 and digit_1 != guess_2) or \
     (digit_3 == guess_2 and digit_2 != guess_1 and digit_1 != guess_3) or \
     (digit_3 == guess_2 and digit_2 != guess_3 and digit_1 != guess_1) or \
     (digit_3 == guess_3 and digit_2 != guess_2 and digit_1 != guess_1) or \
     (digit_3 == guess_3 and digit_2 != guess_1 and digit_1 != guess_2):
    print("Congrats! You win RM1,000!") 
else:
    print("I regret to inform you that your ticket did not win a prize this time.")