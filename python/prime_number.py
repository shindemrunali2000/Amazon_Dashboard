num=13
if num>1:
    for i in range(2 , num//2+1):
      if (num%i)==0:
        print("This Number is not prime")
    else:
        print("This Number is Prime")