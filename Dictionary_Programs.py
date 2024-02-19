#--Dictionary Programs--
#Program 1
    # Function to extract unique values from dictionary values
def extract_unique_values(d):
    unique_values = set(value for values in d.values() for value in values)
    return list(unique_values)

my_dict = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5]}
result = extract_unique_values(my_dict)
print(f"Unique values in dictionary values: {result}")



#Program 2
    # Function to find the sum of all items in a dictionary
def sum_of_dict_items(d):
    result = sum(value for values in d.values() for value in values)
    return result

my_dict = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [3, 4, 5]}
result = sum_of_dict_items(my_dict)
print(f"Sum of all items in the dictionary: {result}")



#Program 3
    # Function to remove a key from dictionary
def remove_key_from_dict(d, key_to_remove):
    d.pop(key_to_remove, None)
    return d

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'
result = remove_key_from_dict(my_dict, key_to_remove)
print(f"Dictionary after removing key '{key_to_remove}': {result}")



#Program 4
from operator import itemgetter

    # Function to sort list of dictionaries by values using itemgetter
def sort_dict_list_by_values(d_list, key_to_sort):
    result = sorted(d_list, key=itemgetter(key_to_sort))
    return result

list_of_dicts = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 22}]
key_to_sort = 'age'
result = sort_dict_list_by_values(list_of_dicts, key_to_sort)
print(f"Sorted list of dictionaries by '{key_to_sort}': {result}")



#Program 5
    # Function to sort list of dictionaries by values using lambda function
def sort_dict_list_by_values_lambda(d_list, key_to_sort):
    result = sorted(d_list, key=lambda x: x[key_to_sort])
    return result

list_of_dicts = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 22}]
key_to_sort = 'age'
result = sort_dict_list_by_values_lambda(list_of_dicts, key_to_sort)
print(f"Sorted list of dictionaries by '{key_to_sort}': {result}")



#Program 6
    # Function to merge two dictionaries
def merge_two_dicts(dict1, dict2):
    result = {**dict1, **dict2}
    return result

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
result = merge_two_dicts(dict1, dict2)
print(f"Merged Dictionary: {result}")



#Program 7
    # Function to convert key-values list to flat dictionary
def convert_to_flat_dict(kv_list):
    result = dict(kv_list)
    return result

key_values_list = [('a', 1), ('b', 2), ('c', 3)]
result = convert_to_flat_dict(key_values_list)
print(f"Converted Flat Dictionary: {result}")



#Program 8
from collections import OrderedDict

    # Function to insert key-value at the beginning in OrderedDict
def insert_at_beginning(od, key, value):
    od.move_to_end(key, last=False)
    od[key] = value
    return od

ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
key_to_insert = 'x'
value_to_insert = 10
result = insert_at_beginning(ordered_dict, key_to_insert, value_to_insert)
print(f"OrderedDict after inserting at the beginning: {result}")



#Program 9
from collections import OrderedDict

    # Function to check order of characters in a string using OrderedDict
def check_order_of_characters(s, pattern):
    od = OrderedDict.fromkeys(s)
    return ''.join(od.keys()) == pattern

input_string = "python"
pattern_to_check = "pthony"
if check_order_of_characters(input_string, pattern_to_check):
    print(f"Order of characters in '{input_string}' matches the pattern '{pattern_to_check}'.")
else:
    print(f"Order of characters in '{input_string}' does not match the pattern '{pattern_to_check}'.")



#Program 10
from collections import Counter

    # Function to find the winner of the election using dictionary and counter
def find_election_winner(votes):
    vote_counts = Counter(votes)
    max_votes = max(vote_counts.values())
    winners = [candidate for candidate, votes in vote_counts.items() if votes == max_votes]
    return winners

election_votes = ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice', 'Charlie']
result = find_election_winner(election_votes)
print(f"Winner(s) of the election: {result}")



#Program 11
    # Function to append dictionary keys and values (in order) in a new dictionary
def append_keys_values_in_order(d):
    result = {}
    for key, value in sorted(d.items()):
        result[key] = value
    return result

my_dict = {'b': 2, 'a': 1, 'c': 3}
result = append_keys_values_in_order(my_dict)
print(f"Dictionary with keys and values appended in order: {result}")



#Program 12
    # Function to sort a dictionary by keys or values
def sort_dict_by_key_or_value(d, by_key=True):
    result = dict(sorted(d.items(), key=lambda x: x[0] if by_key else x[1]))
    return result

my_dict = {'b': 2, 'a': 1, 'c': 3}
result_by_key = sort_dict_by_key_or_value(my_dict, by_key=True)
result_by_value = sort_dict_by_key_or_value(my_dict, by_key=False)
print(f"Dictionary sorted by key: {result_by_key}")
print(f"Dictionary sorted by value: {result_by_value}")



#Program 13
    # Function to sort dictionary key and values list
def sort_dict_key_values_list(d):
    result = {key: sorted(values) for key, values in d.items()}
    return result

my_dict = {'b': [2, 1, 3], 'a': [1, 3, 2], 'c': [3, 2, 1]}
result = sort_dict_key_values_list(my_dict)
print(f"Dictionary with key and values list sorted: {result}")



#Program 14
    # Function to handle missing keys in Python dictionaries
def handle_missing_keys(d, key, default_value):
    result = d.get(key, default_value)
    return result

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'd'
default_value = 0
result = handle_missing_keys(my_dict, key_to_check, default_value)
print(f"Value for key '{key_to_check}': {result}")



#Program 15
    # Function to create a dictionary with keys having multiple inputs
def dict_with_multiple_inputs(keys, values):
    result = dict(zip(keys, values))
    return result

keys_list = ['a', 'b', 'c']
values_list = [1, 2, 3]
result = dict_with_multiple_inputs(keys_list, values_list)
print(f"Dictionary with keys having multiple inputs: {result}")



#Program 16
    # Function to print anagrams together in Python using List and Dictionary
def print_anagrams_together(words):
    anagrams_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams_dict:
            anagrams_dict[sorted_word].append(word)
        else:
            anagrams_dict[sorted_word] = [word]
    return list(anagrams_dict.values())

word_list = ['listen', 'silent', 'enlist', 'heart', 'earth', 'haters']
result = print_anagrams_together(word_list)
print(f"Anagrams grouped together: {result}")



#Program 17
from collections import OrderedDict

    # Function to find the K'th non-repeating character using List Comprehension and OrderedDict
def kth_non_repeating_character(s, k):
    char_count = OrderedDict.fromkeys(s, 0)
    for char in s:
        char_count[char] += 1
    non_repeating_chars = [char for char, count in char_count.items() if count == 1]
    if len(non_repeating_chars) >= k:
        return non_repeating_chars[k - 1]
    else:
        return "No K'th non-repeating character found."

input_string = "geeksforgeeks"
k_value = 3
result = kth_non_repeating_character(input_string, k_value)
print(f"K'th non-repeating character: {result}")



#Program 18
    # Function to check if binary representations of two numbers are anagram
def are_binary_anagrams(num1, num2):
    bin_num1 = bin(num1)[2:]
    bin_num2 = bin(num2)[2:]
    return sorted(bin_num1) == sorted(bin_num2)

number1 = 8
number2 = 4
result = are_binary_anagrams(number1, number2)
print(f"Binary representations of {number1} and {number2} are {'anagrams' if result else 'not anagrams'}.")



#Program 19
from collections import Counter

    # Function to find the size of the largest subset of anagram words using Counter
def largest_anagram_subset_size(words):
    anagram_counts = Counter(tuple(sorted(word)) for word in words)
    max_size = max(anagram_counts.values(), default=0)
    return max_size

word_list = ['cat', 'dog', 'tac', 'god', 'act']
result = largest_anagram_subset_size(word_list)
print(f"Size of the largest subset of anagram words: {result}")



#Program 20
    # Function to remove all duplicate words from a given sentence
def remove_duplicates_from_sentence(sentence):
    words = sentence.split()
    unique_words = list(set(words))
    result = ' '.join(unique_words)
    return result

input_sentence = "Python is great and Python is versatile"
result = remove_duplicates_from_sentence(input_sentence)
print(f"Sentence after removing duplicate words: {result}")



#Program 21
    # Function to find mirror characters in a string using a dictionary
def find_mirror_characters(s):
    mirror_dict = {'p': 'q', 'q': 'p', 'b': 'd', 'd': 'b'}
    result = ''.join(mirror_dict[char] if char in mirror_dict else char for char in s[::-1])
    return result

input_string = "pqbd"
result = find_mirror_characters(input_string)
print(f"Mirror characters in the string: {result}")



#Program 22
    # Function to count the frequencies in a list using dictionary
def count_frequencies_in_list(lst):
    freq_dict = {}
    for element in lst:
        freq_dict[element] = freq_dict.get(element, 0) + 1
    return freq_dict

input_list = [1, 2, 2, 3, 1, 4, 2, 5, 3, 1]
result = count_frequencies_in_list(input_list)
print(f"Frequencies in the list: {result}")



#Program 23
    # Function to convert a list of tuples into a dictionary
def list_of_tuples_to_dict(tuple_list):
    result_dict = dict(tuple_list)
    return result_dict

tuple_list = [('a', 1), ('b', 2), ('c', 3)]
result = list_of_tuples_to_dict(tuple_list)
print(f"Dictionary from a list of tuples: {result}")



#Program 24
from collections import Counter

    # Function to make a string using deletion and rearrangement using Counter and dictionary intersection
def make_string_with_deletion_and_rearrangement(str1, str2):
    counter_str1 = Counter(str1)
    counter_str2 = Counter(str2)
    common_chars = list((counter_str1 & counter_str2).elements())
    result = ''.join(common_chars)
    return result

string1 = "aabbc"
string2 = "ab"
result = make_string_with_deletion_and_rearrangement(string1, string2)
print(f"String made using deletion and rearrangement: {result}")



#Program 25
from collections import Counter

    # Function to check if frequencies can become the same using dictionary, set, and counter
def can_frequencies_become_same(lst):
    freq_counter = Counter(lst)
    unique_freqs = set(freq_counter.values())
    return len(unique_freqs) == 1

input_list = [4, 2, 2, 3, 3, 3]
result = can_frequencies_become_same(input_list)
print(f"Can frequencies become the same: {result}")



#Program 26
    # Assuming a sample dictionary is available as `dictionary_data`
    # Function to scrape and find ordered words in a dictionary
def find_ordered_words(dictionary_data):
    ordered_words = [word for word in dictionary_data if list(word) == sorted(word)]
    return ordered_words

sample_dictionary = ['apple', 'banana', 'orange', 'carrot', 'zebra']
result = find_ordered_words(sample_dictionary)
print(f"Ordered words in the dictionary: {result}")



#Program 27
    # Function to find possible words using given characters in Python
def possible_words_using_characters(word_list, given_chars):
    possible_words = [word for word in word_list if set(word).issubset(set(given_chars))]
    return possible_words

dictionary_words = ['apple', 'banana', 'orange', 'carrot', 'zebra']
given_characters = 'abnroge'
result = possible_words_using_characters(dictionary_words, given_characters)
print(f"Possible words using given characters: {result}")



#Program 28
    # Function to get keys associated with values in a dictionary
def keys_associated_with_values(input_dict, target_value):
    keys_list = [key for key, value in input_dict.items() if value == target_value]
    return keys_list

my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
target_value = 1
result = keys_associated_with_values(my_dict, target_value)
print(f"Keys associated with value {target_value}: {result}")
