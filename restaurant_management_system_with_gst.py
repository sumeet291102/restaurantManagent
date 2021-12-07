def total():
    sum=0
    for i in range(1,16):
        temp=arr2[i]*arr3[i]
        if(arr3[i])!=0: print(arr1[i] + ": " + str(temp))
        sum+=(temp)
    return sum

def recipt():
    print("YOUR BILL")
    cost= total()
    gst= cost*0.05
    serCharge= cost*0.06
    tcost= cost+gst+serCharge
    print("subtotal: " + str(cost))
    print("gst applied: " + str(gst))
    print("service charges applied: " + str(serCharge)) 
    print("total payable amount: " + str(tcost))

def reset():
    for i in range(1,len(arr3)):
         arr3[i]=0
         
def choice(a):
    if(a==0):
        return 1
    elif(a==1):
        reset()
        return 1
    elif(a==2):
        return 0
    elif(a==3):
        recipt()
        return 0
    else: 
        print("choose a valid option!!")

def menu():
    for i in range(0,len(arr1)):
        print(arr1[i])

arr1=["MENU","Pizza","Fries","Sandwich","Pasta","Nachos","Soup","Salad","Coffee","Tea","Mojito","Shake","Lemonade","Coke","Soda","Juice"]
arr2=[0,200,40,60,100,40,60,60,20,20,80,80,80,40,40,40]
arr3=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

while(1):
    menu()
    order=input("place your order 1 at a time: ")
    order=order.capitalize()
    quantity=int(input("quantity: "))
    for i in range(1,len(arr1)):
        if(order==arr1[i]):
            arr3[i]+=quantity
            break
    if(order!=arr1[i] and i==(len(arr1)-1)): 
        print("invalid choice order again!!")
        continue
    print("To continue your ordering press 0")
    print("To reset your order press 1")
    print("To quit press 2")
    print("To print the bill press 3")
    ch=int(input("enter a number btw '0-3'"))
    cho=choice(ch) 
    if(cho==0): 
        print("thanks for ordering😊😊")
        break

