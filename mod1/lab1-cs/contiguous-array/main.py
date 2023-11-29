import sys
def doSomething(inval):
    l = len(inval)
    upper = 0
    lower = 0
    digits = 0
    others = 0
    for i in inval:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        elif i.isdigit():
            digits +=1
        else:
            others +=1
    
    
    print(round(upper*100/l,3),"%")
    print(round(lower*100/l,3),"%")
    print(round(digits*100/l,3),"%")
    print(round(others*100/l,3),"%")
    
    
inputVal = input()    
doSomething(inputVal)
