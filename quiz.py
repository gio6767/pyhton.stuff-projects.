 #quizgame

print("hey buddy whats your name?")
name = input("write your name here: ")
print(f"welcome to mini show {name}!")
print("this is 5 quiz game where u need to answer")

ready = input("r u ready? yes/no: ")

if ready == "no":
    print("alright, maybe next time!")

elif ready == "yes":
    while True:
        score = 0

        print("okay here is your first question ->>")

        question1 = input("whats the biggest planet in our solar system?: ")

        if question1.lower() == "jupiter":
            print("yeahh thats right")
            score += 1
        else:
            print("nah bro")

        question2 = input("r u gay yes/no?: ")

        if question2.lower() == "yes":
            score += 1
            print("yeah bro 😭")
        else:
            print("nah bro")

        question3 = input("do u like rezo? yes/no: ")

        if question3.lower() == "yes":
            print("yeah me too")
            score += 1
        else:
            print("aw hell naw")

        question4 = input("who won in our minecraft pvp? me/you: ")

        if question4.lower() == "you":
            print("yes i did dumbass")
            score += 1
        else:
            print("no i won!")

        question5 = input("r u a femboy? yes/no: ")

        if question5.lower() == "yes":
            print("yeah i know")
            score += 1
        else:
            print("stop lying")

        print(f"nice job bro u got {score}/5 points! see u later")

        again = input("wanna play again? yes/no: ")

        if again.lower() != "yes":
            break

else:
    print("bro just type yes or no ")
