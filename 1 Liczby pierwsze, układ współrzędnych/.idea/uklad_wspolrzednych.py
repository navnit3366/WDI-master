print("Podaj wspolrzedna x: ", end=' ')
x=int(input())
print("Podaj wspolrzedna y: ", end=' ')
y=int(input())

if(x>0 and y>0):
    print("Cwiartka I")
elif(x<0 and y>0):
    print("Cwiartka II")
elif(x<0 and y<0):
    print("Cwiartka III")
elif(x>0 and y<0):
    print("Cwiartka IV")
else:
    print("Na osi")
