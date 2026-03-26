import random
a = random.randint(1,100)
guesses=1
user_input = 0
while(user_input!=a):
    user_input = int(input("Guess The Number: "))
    if(user_input>a):
        print("Too Large")
        guesses+=1
    elif(user_input<a):
        print("Too small")
        guesses+=1
print(f"You have guessed correct number {a} in {guesses} attempts.")
