import time

print("\nHey! Welcome to my quiz!\n")

play = input("Do you want to play? ")

if play.lower() != "yes":
    print("See you later!")
    quit()

print("Okay! Let's play ")
print("...preparing the game...")
score = 0

## Question 1
answer = input("What is the world's longest river called? ")

if answer.lower() == "nile":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

## Question 2
answer = input("Which planet is closest to Earth? ")

if answer.lower() == "venus":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

## Question 3
answer = input("What language is the most popularly spoken worldwide? ")

if answer.lower() == "chinese":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

## Question 4
answer = input("What city is known as the City of Love? ")

if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

## Question 5
answer = input("How many days are in a leap year? ")

if answer.lower() == "366":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

## Question 6
answer = input("Who founded Microsoft? ")

if answer.lower() == "bill gates":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

## Question 7
answer = input("Which country is known to consume the most chocolate? ")

if answer.lower() == "switzerland":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

## Question 8
answer = input("What blonde-haired singer sings the song “You Belong With Me”? ")

if answer.lower() == "taylor swift":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

## Question 9
answer = input("What's the name of the company that published the Mario Kart video game? ")

if answer.lower() == "nintendo":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Okay, this is your last question...")
ready = input("Are you ready? ")

if ready == "no":
    print("Well, I'll give you a few seconds")
    time.sleep(5)
    print("Time is up!")
    time.sleep(2)

## Question 10
answer = input("In Greek mythology, who had snakes for hair and could turn people into stone if they looked at her? ")

if answer.lower() == "medusa":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

if score == 10:
    print("\nCongrats!! You did an excellent job!! You got " + str(score) + "/10 or " + str(score/10 * 100) + "% :)")
elif score >= 7 and score <= 9:
    print("\nWow! You did great! You got " + str(score) + "/10 or " + str(score/10 * 100) + "%")
elif score >= 4 and score <= 6:
    print("\nThat was good! You got " + str(score) + "/10 or " + str(score/10 * 100) + "%")
elif score <= 3:
    print("\nOh, that's okay, you will do better next time! You got " + str(score) + "/10 or " + str(score/10 * 100) + "%")

print("\nI hope you had fun, thanks for playing!")