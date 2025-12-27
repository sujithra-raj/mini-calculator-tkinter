hist="history.txt"
def add(a,b,f):
    res=a+b
    rec=f"{a}+{b}={res}"
    with open(f, "a") as file:
        file.write(rec + "\n")
    print (rec)
    return rec
def sub(a,b,f):
    res=a-b
    rec=f"{a}-{b}={res}"
    with open(f, "a") as file:
        file.write(rec + "\n")
    print(rec)
    return rec
def mul(a,b,f):
    res=a*b
    rec=f"{a}*{b}={res}"
    with open(f, "a") as file:
        file.write(rec + "\n")
    print(rec)
    return rec
def div(a,b,f):
    res=a/b
    rec=f"{a}/{b}={res}"
    with open(f, "a") as file:
        file.write(rec + "\n")
    print(rec)
    return rec
def history(file):
    try:
        with open(file,"r") as f:
            l=f.readlines()
            if not l:
                print("no calculations performed.")
            else:
                for ide,i in enumerate(l,start=1):
                    print(f"{ide}.{i.strip()}")
    except FileNotFoundError:
        print("file finding error")
while True:
    print(" 1.add \n 2.subtract \n 3.multiply \n 4.divide \n 5.view history \n 6.clear history")
    su_input = input("enter option number only (or 'q' to quit): ")
    if su_input.lower() == "q":
        print("Exiting calculator. Bye!")
        break
    else:
        if not su_input.isdigit():
            print("wrong input")
            continue
    su = int(su_input)
         
    if su in (1,2,3,4):
        a= int(input("enter first number: "))
        b= int(input("enter second number: "))
        if su==1:
            add(a,b,hist)
        elif su==2:
            sub(a,b,hist)
        elif su==3:
            mul(a,b,hist)
        elif su==4:
            if b==0:
                print("division by zero not possible.")
            else:
                div(a,b,hist)
    elif su==5:
         history(hist)
    elif su==6:
        open(hist,"w").close()
        print("history cleared.")
    else:
        print("wrong input")
    ans=input("do you want to continue?(y/n):" )
    if ans.lower() !="y":
        break
                    
                
