#--String Programs--
#Program 1
    # Function to check if a string is palindrome
def is_palindrome(s):
    return s == s[::-1]

input_string = "radar"
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")



#Program 2
    # Function to check if a string is both symmetrical and palindrome
def is_symmetrical_and_palindrome(s):
    return s == s[::-1] and s == s[::-1]

input_string = "level"
if is_symmetrical_and_palindrome(input_string):
    print(f"{input_string} is both symmetrical and palindrome.")
else:
    print(f"{input_string} is not both symmetrical and palindrome.")



#Program 3
    # Function to reverse words in a given string
def reverse_words(s):
    words = s.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string

input_string = "Hello World"
result = reverse_words(input_string)
print(f"Original String: {input_string}")
print(f"String after reversing words: {result}")



#Program 4
    # Function to remove i'th character from a string
def remove_ith_character(s, i):
    result = s[:i] + s[i+1:]
    return result

input_string = "example"
index_to_remove = 3
result = remove_ith_character(input_string, index_to_remove)
print(f"Original String: {input_string}")
print(f"String after removing {index_to_remove}th character: {result}")



#Program 5
    # Function to check if a substring is present in a given string
def is_substring_present(main_string, substring):
    return substring in main_string

main_string = "programming"
substring_to_check = "gram"
if is_substring_present(main_string, substring_to_check):
    print(f"{substring_to_check} is present in the string.")
else:
    print(f"{substring_to_check} is not present in the string.")



#Program 6
    # Function to find word frequency in a string using shorthand
def word_frequency(s):
    word_count = {word: s.count(word) for word in set(s.split())}
    return word_count

input_string = "python is easy and python is powerful"
result = word_frequency(input_string)
print("Word Frequency in the string:")
for word, count in result.items():
    print(f"{word}: {count}")



#Program 7
    # Function to convert snake_case to PascalCase
def snake_case_to_pascal_case(snake_case_string):
    words = snake_case_string.split('_')
    pascal_case_string = ''.join(word.capitalize() for word in words)
    return pascal_case_string

snake_case_str = "my_variable_name"
pascal_case_str = snake_case_to_pascal_case(snake_case_str)
print(f"Snake Case: {snake_case_str}")
print(f"Pascal Case: {pascal_case_str}")



#Program 8
    # Method 1: Using len() function
string_len1 = len("Hello")

    # Method 2: Using loop to count characters
string_len2 = 0
for char in "Hello":
    string_len2 += 1

    # Method 3: Using list comprehension and len()
string_len3 = len([char for char in "Hello"])

    # Method 4: Using str.count()
string_len4 = "Hello".count('')

print(f"Length using Method 1: {string_len1}")
print(f"Length using Method 2: {string_len2}")
print(f"Length using Method 3: {string_len3}")
print(f"Length using Method 4: {string_len4}")



#Program 9
    # Function to print even length words in a string
def even_length_words(s):
    words = s.split()
    even_length_words_list = [word for word in words if len(word) % 2 == 0]
    return even_length_words_list

input_string = "Python is amazing and versatile"
result = even_length_words(input_string)
print("Even length words in the string:", result)



#Program 10
    # Function to check if a string contains all vowels
def contains_all_vowels(s):
    vowels = set("aeiou")
    return set(s.lower()) >= vowels

input_string = "education"
if contains_all_vowels(input_string):
    print(f"{input_string} contains all vowels.")
else:
    print(f"{input_string} does not contain all vowels.")



#Program 11
    # Function to count the number of matching characters in a pair of strings
def count_matching_characters(str1, str2):
    common_characters = set(str1) & set(str2)
    return len(common_characters)

string1 = "hello"
string2 = "world"
result = count_matching_characters(string1, string2)
print(f"Number of matching characters between '{string1}' and '{string2}': {result}")



#Program 12
    # Function to remove all duplicates from a given string
def remove_duplicates(s):
    result = ''.join(sorted(set(s), key=s.index))
    return result

input_string = "programming"
result = remove_duplicates(input_string)
print(f"Original String: {input_string}")
print(f"String after removing duplicates: {result}")



#Program 13
    # Function to find the least frequent character in a string
def least_frequent_character(s):
    character_count = {char: s.count(char) for char in set(s)}
    least_frequent_char = min(character_count, key=character_count.get)
    return least_frequent_char

input_string = "programming"
result = least_frequent_character(input_string)
print(f"Least frequent character in the string: {result}")



#Program 14
    # Function to find the maximum frequency character in a string
def maximum_frequency_character(s):
    character_count = {char: s.count(char) for char in set(s)}
    max_frequency_char = max(character_count, key=character_count.get)
    return max_frequency_char

input_string = "programming"
result = maximum_frequency_character(input_string)
print(f"Maximum frequency character in the string: {result}")



#Program 15
    # Function to check if a string contains any special character
def contains_special_character(s):
    special_characters = set("!@#$%^&*()-+")
    return any(char in special_characters for char in s)

input_string = "Hello@World"
if contains_special_character(input_string):
    print(f"{input_string} contains at least one special character.")
else:
    print(f"{input_string} does not contain any special character.")



#Program 16
import random
import string

    # Function to generate random strings until a given string is generated
def generate_random_string(target_string):
    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(target_string)))
    while random_string != target_string:
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(len(target_string)))
    return random_string

target_string = "hello"
result = generate_random_string(target_string)
print(f"Random string generated: {result}")



#Program 17
    # Function to find words greater than given length in a string
def words_greater_than_length(s, k):
    words = s.split()
    result_words = [word for word in words if len(word) > k]
    return result_words

input_string = "Python programming is fun and versatile"
length_threshold = 3
result = words_greater_than_length(input_string, length_threshold)
print(f"Words greater than {length_threshold} characters in the string:", result)



#Program 18
    # Function to remove i-th character from a string
def remove_ith_character(s, i):
    result = s[:i] + s[i+1:]
    return result

input_string = "example"
index_to_remove = 3
result = remove_ith_character(input_string, index_to_remove)
print(f"Original String: {input_string}")
print(f"String after removing {index_to_remove}th character: {result}")



#Program 19
    # Function to split and join a string
def split_and_join(s, delimiter=' '):
    words = s.split(delimiter)
    joined_string = '-'.join(words)
    return joined_string

input_string = "Python is awesome"
result = split_and_join(input_string)
print(f"Original String: {input_string}")
print(f"String after split and join: {result}")



#Program 20
    # Function to check if a given string is a binary string
def is_binary_string(s):
    return all(char in '01' for char in s)

binary_string = "101001"
if is_binary_string(binary_string):
    print(f"{binary_string} is a binary string.")
else:
    print(f"{binary_string} is not a binary string.")



#Program 21
    # Function to find uncommon words from two strings
def find_uncommon_words(str1, str2):
    words1 = set(str1.split())
    words2 = set(str2.split())
    uncommon_words = words1.symmetric_difference(words2)
    return list(uncommon_words)

string1 = "Python programming is fun"
string2 = "Python is versatile"
result = find_uncommon_words(string1, string2)
print(f"Uncommon words between '{string1}' and '{string2}': {result}")



#Program 22
    # Function to replace duplicate occurrences in a string
def replace_duplicate_occurrence(s):
    seen = set()
    result = []
    for char in s:
        if char in seen:
            result.append('$')
        else:
            result.append(char)
            seen.add(char)
    return ''.join(result)

input_string = "programming"
result = replace_duplicate_occurrence(input_string)
print(f"Original String: {input_string}")
print(f"String after replacing duplicate occurrences: {result}")



#Program 23
    # Function to replace multiple words with K in a string
def replace_multiple_words_with_k(s, words_to_replace, k):
    for word in words_to_replace:
        s = s.replace(word, k)
    return s

input_string = "Python is awesome and Python is versatile"
words_to_replace = ["Python", "awesome", "versatile"]
replacement_word = "K"
result = replace_multiple_words_with_k(input_string, words_to_replace, replacement_word)
print(f"Original String: {input_string}")
print(f"String after replacing words with '{replacement_word}': {result}")



#Program 24
from itertools import permutations

# Function to find permutations of a given string using inbuilt function
def find_permutations(s):
    result = [''.join(perm) for perm in permutations(s)]
    return result

input_string = "ABC"
result = find_permutations(input_string)
print(f"Permutations of '{input_string}': {result}")



#Program 25
import re

# Function to check for a URL in a string
def contains_url(s):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return bool(url_pattern.search(s))

input_string = "Check out this website: https://www.example.com"
if contains_url(input_string):
    print(f"{input_string} contains a URL.")
else:
    print(f"{input_string} does not contain a URL.")



#Program 26
    # Function to execute a string of code in Python
def execute_code(code_string):
    exec(code_string)

code_to_execute = "print('Hello, World!')"
execute_code(code_to_execute)



#Program 27
    # Function to rotate a string using string slicing
def rotate_string(s, k):
    rotated_string = s[k:] + s[:k]
    return rotated_string

input_string = "Python"
rotation_count = 2
result = rotate_string(input_string, rotation_count)
print(f"Original String: {input_string}")
print(f"String after rotating {rotation_count} positions: {result}")



#Program 28
    # Function to check if a string can become empty by recursive deletion
def can_become_empty(s):
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return not s

# Example usage:
input_string = "{[()]}"
if can_become_empty(input_string):
    print(f"{input_string} can become empty by recursive deletion.")
else:
    print(f"{input_string} cannot become empty by recursive deletion.")



#Program 29
from collections import Counter

# Function to find all duplicate characters in a string using Counter
def find_duplicate_characters(s):
    char_count = Counter(s)
    duplicate_characters = [char for char, count in char_count.items() if count > 1]
    return duplicate_characters

input_string = "programming"
result = find_duplicate_characters(input_string)
print(f"Duplicate characters in the string: {result}")



#Program 30
    # Function to replace all occurrences of a substring in a string
def replace_substring(s, old_substring, new_substring):
    result = s.replace(old_substring, new_substring)
    return result

input_string = "Python is easy. Python is versatile. Python is fun."
old_substring = "Python"
new_substring = "Java"
result = replace_substring(input_string, old_substring, new_substring)
print(f"Original String: {input_string}")
print(f"String after replacing '{old_substring}' with '{new_substring}': {result}")
