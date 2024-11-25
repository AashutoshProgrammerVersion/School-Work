# Exercise 1: Which subject do you love the most? Make the program continue to ask until they very smartly choose Computer Science.

while False:
    Favourite_Subject = input ('What subjects you love the most (apparently its a smart choice to say you like Computer Science or CS according to this exercise): ')
    if Favourite_Subject == 'CS':
        print("Nice, you found you totally favourite subject that will consume your childhood if you have one.")
        break
    if Favourite_Subject == 'Computer Science':
        print("Nice, you found you totally favourite subject that will consume your childhood if you have one.")
        break

# Exercise 2: Change the values of the while loop for a float rather than an int.

number = 1 #You have to declare this first
while number < 15 or number > 20 :
    print("Please enter a decimal number between 15 and 20")
    number = float(input("enter a number:"))