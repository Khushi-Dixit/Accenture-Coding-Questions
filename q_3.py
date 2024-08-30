'''
3. Write a function to validate if the provided two strings are anagrams or not. If the two strings are anagrams, then return ‘yes’. Otherwise, return ‘no’.
Input:

Input 1: 1st string
Input 2: 2nd string

Output:
(If they are anagrams, the function will return ‘yes’. Otherwise, it will return ‘no’.)

Example

Input 1: Listen
Input 2: Silent

Output:
Yes

Explanation

Listen and Silent are anagrams (an anagram is a word formed by rearranging the letters of the other word).
'''

#Solution
def anagrams(input1, input2):
    if len(input1) != len(input2):
        print("No")
        return
    
    count = 0
    input2_list = list(input2)  # Convert input2 to a list to manipulate it

    for i in input1:
        if i in input2_list:
            input2_list.remove(i)  # Remove the matched character from input2_list
            count += 1
    
    if count == len(input1):
        print("Yes")
    else:
        print("No")

anagrams("Listen", "Silent")



#Solution 2
def anagrams(input1, input2):
    # Convert both strings to lowercase to make the function case-insensitive
    input1 = input1.lower()
    input2 = input2.lower()

    # Check if sorted versions of both strings are the same
    if sorted(input1) == sorted(input2):
        print("Yes")
    else:
        print("No")

anagrams("Listen", "Silent")
