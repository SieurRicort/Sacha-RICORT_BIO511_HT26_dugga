#!usr/bin/python3

#Import modules
import pandas as pd # Used question 3
from plotnine import * # Used to plot in question 3
import random # Used in question 4

# Question 1
## 1.a

my_name = input("SAY MY NAME: ") # my_name is attributed the string sacha

## 1.b

print(f" the length of my name is: {len(my_name)}") # I used fprint to print both text and commands

## 1.c

"""
TO MAKE THE SCRIPT WORK YOU NEED TO PROVIDE AN ARGUMENT, THE NAME OF THE PNG YOU WILL SAVE YOUR PLOT IN
exemple below
python3 dugga.py "a"
"""

def count_letter(my_name, my_letter): # Define the function
    count = 0 # Count is set to 0
    letters=list(my_name) # Letters is the list containing every letters of my name as a one character string
    for letter in letters: # Loops through those letters
        if letter.casefold() == my_letter.casefold(): # Checks if the letter of my name matches the input. casefold() module for case insensitive search
            count += 1 # Do +1 to count every time it matches
        else: continue # Else iterate and check for another letter
    if count == 0:
        print(f"The letter you input is not in the name {my_name}") # Print count, excepted result 2 for a
    else: print(f"The letter you input has been found {count} times in {my_name}.") # Print count, excepted result 2 for a

    return (count)

count_letter('SACHA', 'a') # The function wants a name and a letter
# Question 2

my_list = [1,5,"4","six", 3.14] # Import the list for the exercise

## 2.1
new_list=[] # Create an empty list

for value in my_list: # Go through every  value of my_list
    try:
        new_list.append(int(value)) # If the conversion is possible, append the conversion to new_list
    except ValueError:
        print(f"The {type(value)} {value} in the list is not convertible, skipping it.") # If the conversion is not possible print a message and continue the loop

print(new_list) # Printing the list after going through all my_list

## 2.2
def clean_list(input_a_list): # Define the function, one input needed inside ()
    new_list=[] # Create an empty list

    for value in input_a_list: # Go through every  value of my_list
        try:
            new_list.append(int(value)) # If the conversion is possible, append the conversion to new_list
        except ValueError:
            print(f"The {type(value)} {value} in the list is not convertible, skipping it.") # If the conversion is not possible print
    return new_list

print(clean_list(my_list)) # Use this to print the value return, efficient especially when a global variable has the same name of what is returned.

## 2.3
def sum_neighbors(numbers):

    sum_neighbors=[] # Create a new list
    sum = 0 # Set up a variable
    length = len(numbers) # Get the length of the list in input
    i=0 # To not get stuck in while loop

    while i < (length-1): # Go through every number in the list but stop at the one before last value 
        sum = numbers[i] + numbers[i+1] # Calculate the sum of neighbors
        sum_neighbors.append(sum) # Append the result to the result variable
        i += 1 # To break the loop once new_list[i] = the one before max.index

    return sum_neighbors

print(f"The results of summing neighbors is equel to: {sum_neighbors(new_list)}.") # Input is newlist from 2.1

# Question 3

def i_love_plotnine(data_file,input_x,input_y,output_name):
    
    df = pd.read_csv(data_file) # Used pandas to read csv and transform it to a panda dataframe

    cnv_fig1 = (
        ggplot(df, aes(x=input_x, y=input_y)) # Set what dataframe to use, what is x and y in the plot
        + geom_point() # Type of plot: scatterplot
        + labs(
            title=(f"{input_y} vs {input_x}"),
            x="Position (mb)", # This could be changed to remove _ or spaces between units and the variable's name + capitalize the first letter...
            y="Log2 Ratio", # Same here
        )
    )

    # 3.3

    cnv_fig1.save(
        str(output_name),
        dpi=300
    )
    print(f"The plot has been saved !")

i_love_plotnine('cnv_data.csv', 'position_mb', 'log2_ratio', 'log2_vs_position')
# Question 4

def who_will_win(P1, P2, throws): # Define the function
    winners={ # Setup the winners dictionnary
        P1 : 0,
        P2 : 0,
        'Tie(s)' : 0
    }

    i = 0 # Setup i for a while loop

    while i < throws: # go until i reaches throws
        score_P1 = random.randint(1,6) # RNG int between 1,6 for P1
        score_P2 = random.randint(1,6) # RNG int between 1,6 for P2
        if score_P1 > score_P2: # Checking highest roll between the two
            winners[P1] += 1 # Value of the key P1 +1
        elif score_P2 > score_P1:
            winners[P2] += 1 # Value of the key P1 +1
        else: winners["Tie(s)"] += 1 # Add the possibility of a tie
        i += 1
    return winners # End of the function, return the dictionnary

print(f"Here is a summary of who won: {who_will_win('Alice', 'Bob', int(20))}") # Print the dictionnary containing results