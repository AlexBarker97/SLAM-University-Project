#Python Template for ES2B4 Assignment - 2

#Name: Alex Barker
#ID : U1512136
#Assignment Section : assignment2_a1_2

######## Your Code Below ########
import math
def Tangent(AMin,AMax):
    '''Prints calues for the tangent of an angle in degrees'''
    Tan = [(math.sin(math.radians(x))/math.cos(math.radians(x))) for x in range(AMin,AMax+1)]
    print("Tangent of", AMin, "to", AMax,"degrees in steps of 1 degree: ")
    return(Tan)

def VowelsExtract(INPUT):
    '''Prints a list of the vowles found in an input given in the form: \n VowelsExtract(input to check)'''
    Vowels = ["A","E","I","O","U","a","e","i","o","u"]
    VowelsFound = []
    INPUT = INPUT.lower()
    L = len(INPUT)
    i=0
    while i < L:
        if INPUT[i] in Vowels:
            VowelsFound.append(INPUT[i])
        i+=1
    return("Vowels Found: ",VowelsFound)

def equation(Xmin, Xmax, Ymax):
    '''Prints values for y=x*x+5 in ranges given using inputs:\n xx5(lower x, upper x, upper y) \n note, lower y default 0'''
    x = [x for x in range(Xmin, Xmax+1)]
    y = []
    OutDomain = []
    for i in x:
        y.append(i*i+5)
    L = len(y)
    i=0
    while i < L:
        if (y[i]) > Ymax:
            OutDomain.append(i)
            i+=1
            continue
        else:
            i+=1
            continue
    count=0
    for i in OutDomain:
        y.remove(y[i-count])
        x.remove(x[i-count])
        count+=1
    for i in x:
        return(i,(i*i+5))

print(Tangent(0,89))
print("\n")
print(VowelsExtract("Alex Barker Assignment 2"))
print("\n")
print(equation(-5,5,10))
