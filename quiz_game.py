print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("See you next time")
    quit()

print("Okay! Let's play")
score = 0

answer = input("What does the CPU stand for? ").lower()
if answer == "central processing unit":
    print('Correct! ')
    score += 1
else:
    print('Incorrect! ')

answer = input("What does the GPU stand for? ").lower()
if answer == "graphic processing unit":
    print('Correct! ')
    score += 1

else:
    print('Incorrect! ')

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print('Correct! ')
    score += 1
else:
    print('Incorrect! ')

answer = input("What does PSU stand for? ").lower()
if answer == "Penn State University":
    print('WE ARE! ')
    score += 1
else:
    print('Incorrect! ')

print("You got " + str(score) + " questions correct!")