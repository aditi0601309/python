def disp():
    #a=10
    try:
        a=int(input("enter first number:"))
        b=int(input("enter second number:"))
        c=a/b
        print(c)
    except:
        print("variable not defined,try again")
    else:
        print("nothing went wrong")
    finally:
        print("try except finish")
disp()
