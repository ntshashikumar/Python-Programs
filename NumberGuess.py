import random

count=0
secretnum=random.randint(0,10)
print(secretnum)

while True:
    guess=int(input("Guess the number :"))
    count+=1
    if guess==secretnum:
        print(f"You guessed number correctly and took {count} chances")
        break
    else:
        print("wrong! Try Again")


