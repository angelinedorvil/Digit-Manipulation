from timeit import default_timer as timer
import sys

# TO DO: define your arrange function here...

def arrange(s, even='', odd='', index=0): #create 2 variables to seperate even and odd numbers in a string
    if index == len(s):  #base case when the string ends
        return even + odd
    
    current_digit = s[index] #keeping track of the index in the string, since the strings are different lenghts and the list has different strings
    
    if current_digit.isdigit(): #if it's a number, to triage \n
        if int(current_digit) % 2 == 0: #checking if number is even
            even += current_digit   #assorting to appropriate variable, appending new values
        else:
            odd += current_digit
    
    return arrange(s, even, odd, index + 1) #the arranged numbers per index, so the result for each seperate string

#---- Main Program ----#        
# TO DO: start timer here...
import time

start = time.time()
# starting timer

# DONE: Parse the command line arguments

#C:\Code>python p1.py digits.txt


if len(sys.argv) != 2:
    raise ValueError('Please provide one file name.')
inputFileName = sys.argv[1]

print("\nThe file that will be used for input is: " + inputFileName)


# TO DO: Open file, read lines into a list, close file...

print("\n************************")
print("*** Modified Strings ***")
print("************************")

#open the digits file
c = open("digits.txt", "r")
#read contents of the file into a string
myList = c.readlines()
c.close()

# TO DO: For each item in the list, call arrange() and
#        print the modified list returned by arrange()...

#print (myList) #testing the read raw/original data from files digits

for i in myList:  #going through the items in the data that was printed and applying function to modify list
    result2 = arrange(i)
    print(result2)
    
# TO DO: End timer...
end = time.time()


# TO DO: print the running time...
totalTime = end - start
print("\nTotal time of program: {0} milliseconds".format(totalTime))
