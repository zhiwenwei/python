age_of_zww = 25
count = 0
while count < 3:
    guess_age = int(input("guess_age:"))
    print(type(guess_age))
    if guess_age == age_of_zww:
        print("yes,you got it!!!")
        break
    elif guess_age > age_of_zww:
        print("think smaller...")
    else:
        print("think bigger...")
    count += 1