# Here goes your code for the task
# Name:                 OddAndEvenNumbers.py
# Author:               Meetkumar Patel
# Date Created:         Februarey 20, 2022
# Date Last Modified:   Februaury 21, 2022

# Purpose:
#
#In this program it will allow th user to enter group of numbers and sort them out as odd and even list. 

#welcome screen

print("In this program you can enter integers and the program will be able to check if its odd or even and sort accordingly.")
#Here user inout is stored then mapped on the list 
numbers = input("Please Enter any Number of Integers: \n")
num_List = list(map(int, numbers.split(",")))
#This empty list will be used to store the numbers accordingly thus used to append accordingly.
even_List = []
odd_List = []
separator = " "
#here the loop will run from the user given numbers
for num in num_List:
    #Here the condition checks by using % operand to sort the odd and even
    # if the number gives a reminder of 0 and odd will give 1 
    if num % 2 == 0:
         even_List.append(num)
          
    else:
        odd_List.append(num)

even = separator.join(map(str, even_List))
odd = separator.join(map(str, odd_List))
print("{0:s}{1:^5}{2:^10}".format("Even Numbers are",":", even))
print("{0:s}{1:^7}{2:^5}".format("Odd Numbers are",":", odd))


