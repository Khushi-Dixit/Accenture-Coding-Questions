#take string values and count the similar value than find out the most occured value and print it (basically used to see who won in a tournement like team a or team b)
n=int(input())

l=[]
count=0
count2=0
for i in range(n):
    i=input()
    l.append(i)
l.sort()
for j in l:
    if j in l:
        count+=1
    else:
        count2+=1
if count2>count:
    print(l[0])
else:
    print(l[n-1])
