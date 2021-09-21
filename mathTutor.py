#mathTutor.py
#Christina Okoduwa
#Virtual Math Tutor Program
#Input: The option the user wants to view. The type of math problems, the levels, and the number of problems the user want to work on. 
#
#Processing: 1. Prompts user to selection 1 out of 3 options from the menu. 
#            2. Option 1 will show rules, Option 2 will display the math problems, Option 3 will exit the program. 
#            3. For Option 2 the user will be prompted to select 1 or 3 options for the type of math problems, Addition, Subtraction, or Multiplication. 
#            4. The user will then select the level of math problems, either 1 or 2. 
#            5. The user will enter how many problems they want to work on. 
#            6. Once the answer is submited it will indiciate if it is correct or not. 
#            7. The score will be displayed, then the user can choose from the main menu again.          
#
#Output: Math tutoring program that displays the selection Menu with three options. Different types of problems and levels the user can choose from and practice.  

import random     

print  ("WELCOME TO CHRISTINA'S MATH TUTORING LAB!!!\n\n")  #opening welcome statement to the program.

def main():  #user will select one option to either review the rules, start the problems, or exit the program.
    print("""\nPlease choose from the following menu:
        \n1) See rules
        \n2) Math Practice
        \n3) Exit""")
def MathPractice():  #user will select which type of math problems they will like to practice. 
    print ("""\nPlease choose from the following menu:
        \n1) Addition
        \n2) Subtraction
        \n3) Multiplication""")

def level(): #the user will select the level of the problems they will like to work on. 
    print ("""\nNext, Choose a level,\n
        \n1) Level One (1)
        \n2) Level Two (2)""")


#defining variables 

selected_option = 0  #this is for the options that the user will choose in the beginning menu. 


while selected_option != 3:
    main() #this will call one of the three options in the beginning menu. 
    selected_option = int(input("\nEnter your choice here: ")) #this will prompt the user to put the number of their selection option from the menu. 
    if selected_option == 1: #if the user selects option 1 it will print the rules. 
        print ("This program will help you develop and practice your math skills. You must first select the type of problems, either Addition, Subtraction, or Multiplication." \
               "Then you must choose a level. Level 1 are problems with single digits and level 2 are problems with double digits." \
                "Then you will choose how many problems you will to complete." \
                     "After you have completed all of your problems you will receive a score. You can practice as many times as you like. Enjoy and have fun!")

    elif selected_option == 2: #if the user selects option 2 it will prompt the math practice option. 
        print ("\nYou have chosen to practice some math problems.")
        MathPractice() #this will call the three options for the type of math problems. 
        math_choice = int(input("\nEnter your choice here: ")) #this will prompt the user to input their selection of the type of math problems. 
        level() #this will call the two options for the level of the math problems. 
        level_choice = int(input("\nEnter your level choice here: ")) #this will prompt the user to input their selection of the level for the problems. 
        if level_choice ==1: #when the level is 1. 
            n = int(input("\nEnter how many problems you would like to try: ")) #this will prompt the user to enter how many math problems they want to practice. 
            correct_answer_addition = 0 #this will count the correct amount of addition problems.
            correct_answer_subtraction = 0 #this will count the correct amount of subtraction problems.
            correct_answer_multiplication = 0 #this will count the correct amount of multiplication problems.
            
            if math_choice == 1: #if the user selects 1 the loop below will display the addition problems.
                for math in range(n):
                    a = random.randint(1,9) #selects the first random from 1 to 9 for the operation. 
                    b = random.randint(1,9) #selects the second random from 1 to 9 for the operation. 
                    print ("\nProblem", math+1, ":") #counts the amount of math problems in the loop. 
                    print (a ,"+", b, "? = ", end="") #prints the math problem. 
                    math_answer = int(input()) #prompts user to input their answer. 
                    
                    if math_answer == a + b: #if the user answer is correct 
                        correct_answer_addition += 1 #this will count the amount of correct addition answers.
                        print ("\nCorrect! Great Job!") #will print this statement if the answers are correct. 
                    else:
                        print ("\nSorry that is incorrect. The correct answer is ", (a + b)) #if the answers are incorrect it will this statement and also print the correct answer.
                    percent_correct = ((correct_answer_addition/n)*100) #this will calculate the precentage of the correct addition answers. 
                print ("\nyou answered", correct_answer_addition, "out of ", n, " correctly. Your score =", '%.f'%percent_correct, "%") #will print the statement for the correct amount of answers out of the total problems attempted and will print the total precentage. 
            
            elif math_choice == 2: #if the user selects 2 the loop below will display the subtraction problems.
                for math in range(n):
                    a = random.randint(1,9) #selects the first random from 1 to 9 for the operation. 
                    b = random.randint(1,9) #selects the second random from 1 to 9 for the operation.
                    if a < b: #for subtraction this will make the first number larger than the second number. 
                        a, b = b, a
                    
                    print ("\nProblem", math+1, ":") #counts the amount of math problems in the loop.   
                    print (a ,"-", b, "? = ", end="") #prints the math problem. 
                    math_answer = int(input()) #prompts user to input their answer.
                    if math_answer == a - b: #if the user answer is correct
                        correct_answer_subtraction += 1 #this will count the amount of correct subtraction answers.
                        print ("\nCorrect! Great Job!") #will print this statement if the answers are correct. 
                    else:
                        print ("\nSorry that is incorrect. The correct answer is ", (a - b)) #if the answers are incorrect it will this statement and also print the correct answer.
                    percent_correct = ((correct_answer_subtraction/n)*100) #this will calculate the precentage of the correct subtraction answers. 
                print ("\nyou answered", correct_answer_subtraction, "out of ", n, " correctly. Your score =", '%.f'%percent_correct, "%") #will print the statement for the correct amount of answers out of the total problems attempted and will print the total precentage.
            
            elif math_choice == 3: #if the user selects 1 the loop below will display the multiplication problems.
                for math in range(n):
                    a = random.randint(1,9) #selects the first random from 1 to 9 for the operation. 
                    b = random.randint(1,9) #selects the second random from 1 to 9 for the operation. 
                    print ("\nProblem", math+1, ":") #counts the amount of math problems in the loop. 
                    print (a ,"*", b, "? = ", end="") #prints the math problem. 
                    math_answer = int(input()) #prompts user to input their answer. 
                    if math_answer == a * b: #if the user answer is correct
                        correct_answer_multiplication += 1 #this will count the amount of correct multiplication answers.
                        print ("\nCorrect! Great Job!") #will print this statement if the answers are correct. 
                    else:
                        print ("\nSorry that is incorrect. The correct answer is ", (a * b)) #if the answers are incorrect it will this statement and also print the correct answer.
                    percent_correct = ((correct_answer_multiplication/n)*100) #this will calculate the precentage of the correct multiplication answers. 
                print ("\nyou answered", correct_answer_multiplication, "out of ", n, " correctly. Your score =", '%.f'%percent_correct, "%") #will print the statement for the correct amount of answers out of the total problems attempted and will print the total precentage.
            
        

        if level_choice ==2: #when the level is 2. 
            n = int(input("\nEnter how many problems you would like to try: ")) #this will prompt the user to enter how many math problems they want to practice.
            correct_answer_addition = 0 #this will count the correct amount of addition problems.
            correct_answer_subtraction = 0 #this will count the correct amount of subtraction problems.
            correct_answer_multiplication = 0 #this will count the correct amount of multiplication problems.
            
            if math_choice == 1: #if the user selects 1 the loop below will display the addition problems.
                for math in range(n):
                    a = random.randint(1,99) #selects the first random from 1 to 99 for the operation. 
                    b = random.randint(1,99) #selects the second random from 1 to 99 for the operation. 
                    print ("\nProblem", math+1, ":") #counts the amount of math problems in the loop. 
                    print (a ,"+", b, "? = ", end="") #prints the math problem. 
                    math_answer = int(input()) #prompts user to input their answer. 
                    if math_answer == a + b: #if the user answer is correct
                        correct_answer_addition += 1 #this will count the amount of correct addition answers.
                        print ("Correct! Great Job!") #will print this statement if the answers are correct.
                    else:
                        print ("Sorry that is incorrect. The correct answer is ", (a + b)) #if the answers are incorrect it will this statement and also print the correct answer.
                    percent_correct = ((correct_answer_addition/n)*100) #this will calculate the precentage of the correct addition answers. 
                print ("you answered", correct_answer_addition, "out of ", n ," correctly. Your score =", '%.f'%percent_correct, "%") #will print the statement for the correct amount of answers out of the total problems attempted and will print the total precentage.
                
            elif math_choice == 2: #if the user selects 1 the loop below will display the subtraction problems.
                for math in range(n):
                    a = random.randint(1,99) #selects the first random from 1 to 99 for the operation. 
                    b = random.randint(1,99) #selects the second random from 1 to 99 for the operation. 
                    if a < b: #for subtraction this will make the first number larger than the second number. 
                        a, b = b, a
                    print ("\nProblem", math+1, ":") #counts the amount of math problems in the loop. 
                    print (a ,"-", b, "? = ", end="") #prints the math problem. 
                    math_answer = int(input()) #prompts user to input their answer.
                    if math_answer == a - b: #if the user answer is correct
                        correct_answer_subtraction += 1 #this will count the amount of correct subtraction answers.
                        print ("Correct! Great Job!") #will print this statement if the answers are correct.
                    else:
                        print ("Sorry that is incorrect. The correct answer is ", (a - b)) #if the answers are incorrect it will this statement and also print the correct answer.
                    percent_correct = ((correct_answer_subtraction/n)*100) #this will calculate the precentage of the correct subtraction answers. 
                print ("you answered", correct_answer_subtraction, "out of ", n ," correctly. Your score =", '%.f'%percent_correct, "%") #will print the statement for the correct amount of answers out of the total problems attempted and will print the total precentage.
            
            elif math_choice == 3: #if the user selects 1 the loop below will display the multiplication problems.
                for math in range(n):
                    a = random.randint(1,99) #selects the first random from 1 to 99 for the operation. 
                    b = random.randint(1,99) #selects the second random from 1 to 99 for the operation. 
                    print ("\nProblem", math+1, ":") #counts the amount of math problems in the loop. 
                    print (a ,"*", b, "? = ", end="") #prints the math problem. 
                    math_answer = int(input()) #prompts user to input their answer.
                    if math_answer == a * b: #if the user answer is correct
                        correct_answer_multiplication += 1 #this will count the amount of correct multiplication answers.
                        print ("Correct! Great Job!") #will print this statement if the answers are correct.
                    else:
                        print ("Sorry that is incorrect. The correct answer is ", (a * b)) #if the answers are incorrect it will this statement and also print the correct answer.
                    percent_correct = ((correct_answer_multiplication/n)*100) #this will calculate the precentage of the correct multiplication answers. 
                print ("you answered", correct_answer_multiplication, "out of ", n ," correctly. Your score =", '%.f'%percent_correct, "%") #will print the statement for the correct amount of answers out of the total problems attempted and will print the total precentage.
           

    elif selected_option == 3: #if user selects option 3 it will prompt the program to exit. 
        print("\nThank you for playing. Have a nice day!") #this will print the following exit message. 
    else:
        print ("Invalid input. You must choose 1 or 2 or 3 from the menu") #if the user makes a selection that is not 1, 2, or 3, this will prompt them to make a correct selection. 
    



            



