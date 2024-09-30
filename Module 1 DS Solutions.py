
score = int(input("Enter the score in the math exam: "))
if score> 100:
    print ('Invalid input')
elif score > 90:
    print('your grade is A') 
elif score > 80:
    print('your grade is B')
elif score > 70:
    print('your grade is C')
elif score > 60:
    print('your grade is D')
else:
    print('your grade is F')
    print ('you better work hard')
    
    
'''Q1 •	Create a program to check if a given number is divisible by 4, 5, 6, 7, 8 or 11. 
If the number is not divisible by any of these, then print that it isn’t divisible 
by any of these numbers. Pay attention to outputs and formatting.'''
n = int(input("Enter your number: "))
if any(n % d == 0 for d in [4, 5, 6, 7, 8, 11]):
    print(f'{n} is divisible by one of these numbers: 4, 5, 6, 7, 8, or 11')
else:
    print(f'{n} is not divisible by any of these numbers: 4, 5, 6, 7, 8, or 11')

#Q2 List the letters of the word “apocalypse” and print them out. Hint: strings are lists of letters.
word = "apocalypse"
for l in word:
    print(l)


#Q3 •	List the letters of the word “apocalypse” and print them out. Stop when the letter ‘y’ is encountered.
word = "apocalypse"
for l in word:
    if l == 'y':
        break
    print(l)

#Q4•	List the letters of the word “apocalypse” and print them out. Skip the letter ‘y’ and print them all.
word = "apocalypse"
for letter in word:
    if letter == 'y':
        continue
    print(letter)


#•	Create a list of numbers from 2 to 30, including 30, with increments of 2
list1 = list(range(2, 31, 2))
print(list1)


#•	Create a list of numbers form 100 to -100 in that order. Take gaps of 5.
list2 = list(range(100, -105, -5))
print(list2)

#•	Print out the first 20 values of the multiples of 43.
#o	Using for loop
for i in range(1, 21):
    print(43 * i)

#o	Using a while loop
i = 1
while i <= 20:
    print(43 * i)
    i+=1
    
    
    
#•	Create a list of 10 values containing all different primitive data types in python.

data_list = [True, False, "Diwakar", "Sinha", 42, -1, 3.14, -2.718, 1+2j, -3-4j]

# Printing values at odd positions
for i in range(len(data_list)):
    if i % 2 != 0:
        print(data_list[i])

# Printing the first value
print(data_list[0])

# Printing the last value
print(data_list[-1])

# Printing the last three values
print(data_list[-3:])

#•	Initialize a list containing first 10 multiples of 19 using list comprehension technique.
multiples_of_19 = [19 * i for i in range(1, 11)]
print(multiples_of_19)

#•	Write a program that takes input from the user for temperature in degree Celsius. Return the value in Fahrenheit. Print it out to the user.  
degc = float(input("Enter temperature in Celsius: "))
degf = (degc * 9/5) + 32
print(f'Temperature in degrees Fahrenheit is: {degf}')
















        