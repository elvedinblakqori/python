#Create a list

names = ["Blerta", "Erosi", "Driloni", "Brikena", "Ylli"]

#Iterate in the names list and print every name

for name in names:
    print(name)

    print("hello world")

###############################

sentence = "Hello World"

for character in sentence:
    if character.isalpha(): # Check if the character is a letter
        print(character)


#Range Function

for number in range(1,6):  #print numbers from the number 1 to 5 or more initial n to n-1
    print(number)

############################

numbers = [12, 45, 6, 72, 21, 8,94, 57]

#Initialize a variable "maximum" with the first value from the list "numbers"

maximum = numbers[0]

for num in numbers: #Begin a loop iterating through each element in the list "numbers"
    if num > maximum: #Check if the correct element "num" is grater then the current maximum value
        maximum = num # if so, update the maximum value to be the current element in num
    print("The maximum value in the list is: ", maximum)

#######################
#While loop

Count = 1 # Initialize  the loop control variable

while count <= 5 #The Condition if count is less then or equal to 5
    print("Iteration", count)
    count +=1 #Increment the loop control variable


################################
#Do while loop

#Infinite loop

while True:
    #Prompt user to enter a positive number
    user_input = input("Enter a positive number: ")


    #Check if the input is numeric
    if user_input.isnumeric():
        number = int(user_input)

        if number > 0:
            break

        #Print the error message for invalid input
        print("invalid input please try again")
    #Print the valid positive number entered by the user
    print("You have entered a valid positive number: ", number)


###############################
#break


    numberList = [1,2,3,4,5,6,7]
    target = 4

    for number in list:
        print(number) #Print the current element that is being iterated
        if number == target: #Check if the current element is equal to the target value
            print("Target Found")
            break # End the loop imidiately

