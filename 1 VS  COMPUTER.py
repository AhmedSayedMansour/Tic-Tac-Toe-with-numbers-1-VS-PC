import random
print("      WELCOME TO")
print("TIC-TAC-TOE with numbers")
p1=str(input("player one name:"))
p2="computer"
odd=["1","3","5","7","9"]
even=["0","2","4","6","8"]
m=[["a1","a2","a3"],["b1","b2","b3"],["c1","c2","c3"]]
print(p1+"  you can choose from(1,3,5,7,9) with no Repetition")
p=p1
a=[[-50,-50,-50],[-50,-50,-50],[-50,-50,-50]]
p11=[1,3,5,7,9]
m2=["a1","a2","a3","b1","b2","b3","c1","c2","c3"]
p12=[0,2,4,6,8]
t=111
c=9
while (c>=1):
    while (2!=3):
        for h in range (0,3):
            for k in range (0,1):
                print (m[h][k]," | ",m[h][k+1]," | ",m[h][k+2])
                if h<2 :
                    print("_________________")
        print (p +" trun")
        if (p=="computer"):
            u=random.randint(0,len(m2)-1)
            position=m2[u]
        else:
            position=(input("choose the position: "))
        while (True):
            if (position in m2):
                m2.remove(position)
                break
            else:
                print("Wrong!!")
                position=(input("choose the right position: "))
        for i in range (0,3):
            for g in range(0,3):
                if (position==m[i][g]):
                    break
            if (position==m[i][g]):
                break
        if (t==111):
            print (p11)
            number=(input(p1+" choose right number: "))
            e=True
            z=0
            while e==True:
                for u in range(len(odd)):
                    if number ==odd[u]:
                        odd[u]="asdfg"
                        z=u
                        e=False
                        break
                if odd[z]=="asdfg":
                    e=False
                    break
                else:
                    number= (input(p1+" choose right number: "))
            number=int(number)
            if (number in p11):
                m[i][g]=number
                a[i][g]=number
                p11.remove(number)
                t=222
                p=p2
                c-=1
                break
            else:
                print ("choose right number:")
        if (t==222):
            u=random.randint(0,len(p12)-1)         
            number=p12[u]
            if (number in p12):
                m[i][g]=number
                a[i][g]=number
                p12.remove(number)
                t=111
                p=p1
                c-=1
                break 
            else:
                print ("choose right number:")
    #conditions of winning :\\\
    if(a[0][0]+a[0][1]+a[0][2]==15 or a[1][0]+a[1][1]+a[1][2]==15 or a[2][0]+a[2][1]+a[2][2]==15):
        if (t==222):
            print (p1+" is the winner")
            break
        else:
            print ("YOU LOSE")
            break
    #conditions of winning :- - -
    if(a[0][0]+a[1][0]+a[2][0]==15 or a[0][1]+a[1][1]+a[2][1]==15 or a[0][2]+a[1][2]+a[2][2]==15):
        if (t==222):
            print (p1+" is the winner")
            break
        else:
            print ("YOU LOSE")
            break
    #conditions of winning :/\(x)
    if(a[0][0]+a[1][1]+a[2][2]==15 or a[0][2]+a[1][1]+a[2][0]==15):
        if (t==222):
            print (p1+" is the winner")
            break
        else:
            print ("YOU LOSE")
            break
if c==0:
    print("DRAW")
