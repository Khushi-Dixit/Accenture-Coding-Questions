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
