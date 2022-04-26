str=input("enter any string:")
dict={}
for i in str:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
        print("count all the charectets in entered string is:",dict)
