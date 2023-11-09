import  foodadvicer
g=foodadvicer.foodgen()


def home():
    print("Welcome to the food Advicer app")
    print("1.Morning Breakfast \n 2.Afternoon lunch\n 3.Snacks\n 4.Dinner\n 5.exit()")
    c=int(input("enter your option:  "))
    if c==1:
        x=g.morning()
        print(x)
    elif c==2:
        print("1.Curry\n 2.Sambar\n 3.Rasam")

        sad=int(input("Enter your option:  "))
        if sad==1:
            x=g.curry()
            print(x)
        elif sad==2:
            x=g.sambar()
            print(x)
        elif sad==3:
            x=g.rasam()
            print(x)
        else:
            home()
    elif c==3:
        x=g.snacks()
        print(x)
    elif c==4:
        x=g.dinnner()
        print(x)
    elif c==5:
        exit()



    