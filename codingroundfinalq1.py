#convert the given number in binary and print the sum of its binary digits
n=int(input())
x=n%2
y=n//2
sums=0
while y>=1:
    x=y%2
    sums+=x
    y=y//2
    if y==1:
        sums+=y
    
print(sums)

#example
#15
#4
