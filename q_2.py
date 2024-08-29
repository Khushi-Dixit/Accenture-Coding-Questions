'''2. Execute the given function.
def LargeSmallSum(arr)

The function takes an integral arr which is of the size or length of its arguments. Return the sum of the second smallest element at odd position ‘arr’ and the second largest element at the even position.

Assumption

Every array element is unique.
Array is 0 indexed.
Note:

If the array is empty, return 0.
If array length is 3 or <3, return 0.
 
Example

Input:
Arr: 3 2 1 7 5 4

Output:
7
 

Explanation

The second largest element at the even position is 3.
The second smallest element at the odd position is 4.
The output is 7 (3 + 4).
 '''

#solution

def LargeSmallSum(arr):
    if len(arr)<=3:
        return 0
    even_position=arr[::2]
    odd_position=arr[1::2]
    even=sorted(even_position,reverse=True)
    odd=sorted(odd_position)
    final=odd[1]+even[1]
    return final
arr=[3,2,1,7,5,4]
print(LargeSmallSum(arr))





