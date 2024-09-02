#print even and odd position in string format
def print_even_odd_positions(s):
    even_positions = s[::2]  # Characters at even indices (0-based indexing)
    odd_positions = s[1::2]  # Characters at odd indices (0-based indexing)
    
    print("Even positions:", even_positions)
    print("Odd positions:", odd_positions)

# Sample Input
s = "OpenAI"

# Print even and odd position characters
print_even_odd_positions(s)




#longest decreasing number
def longest_decreasing_subsequence(arr):
    if not arr:
        return []

    longest = []
    current = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            current.append(arr[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [arr[i]]

    # Final check after loop to capture the last subsequence
    if len(current) > len(longest):
        longest = current

    return longest

# Sample Input
arr = [9, 8, 7, 3, 2, 5, 4, 1, 0]

# Get the longest decreasing subsequence
longest_decreasing = longest_decreasing_subsequence(arr)

# Print the result
print("Longest decreasing subsequence:", longest_decreasing)
