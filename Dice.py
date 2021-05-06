import random

text1 = input("Enter \n'0' for normal die \n'1' for special die\n")
if text1 == '0':
    while True:
        l1 = random.randint(1, 6)
        print("You got",l1,"with the roll")
        breaker = input("Enter q/Q to Exit anything else for continue \n")
        if breaker == ('q' or 'Q'):
            print("Exiting die")
            break
elif text1 == '1':
    str1 = int(input("Enter the number you want at more frequency: "))
    if str1 >0 and str1 < 7:
        while True:
            l1 = random.randint(1, 6)
            l2 = [str1,str1,str1,str1,str1,l1]
            new_set = random.choice(l2)
            # print(new_set)
            print("You got",new_set,"with the roll")
            breaker = input("Enter q/Q to Exit anything else for continue \n")
            if breaker == ('q' or 'Q'):
                print("Exiting die")
                break
    else:
        print("Sorry no Such die Found with this number")
    