# vowels = ['a', 'e', 'i', 'o', 'u']
# Index:   0    1    2    3    4

# print(vowels[0])     # Output: a
# print(vowels[1])     # Output: e
# print(vowels[2])     # Output: i
# print(vowels[3])     # Output: o
# print(vowels[4])     # Output: u

# Tvowels = ['a', 'e', 'i', 'o', 'u']
# Index:   0    1    2    3    4
# Index:  -5   -4   -3   -2   -1

# vowels = ['a', 'e', 'i', 'o', 'u']
# print(vowels[0 : 3])
# print(vowels[1 : 3])
# Output:
# ['a', 'e', 'i']
# ['e', 'i']
# It starts from the start index (inclusive) and ends before the end index (non-inclusive). So in the above example, print(vowels[1 : 3]) only returned items at indices 1 and 2, and didn't include index 3.

todo = ['🏦 Get quarters', '🧺 Do laundry', '🌳 Take a walk', '💈 Get a haircut', '🍵 Make some tea', '💻 Complete Lists chapter', '💖 Call mom', '📺 Watch Jujutsu Kaisen']

# Print the first item and the second item. What did you get?
print(todo[0])
print(todo[1])

# Next, use slicing to print the third, fourth, and fifth items.
print(todo[2 : 4])

# Try printing out the item at index 9 to see the IndexError before moving on.
print(todo[9])