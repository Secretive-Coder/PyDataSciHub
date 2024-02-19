#--Tuple Programming--
#Program 1
    # Function to find the size of a Tuple
def tuple_size(t):
    return len(t)

my_tuple = (1, 2, 3, 'a', 'b', 'c')
result = tuple_size(my_tuple)
print(f"Size of the Tuple: {result}")



#Program 2
    # Function to find the maximum and minimum K elements in a Tuple
def max_min_k_elements(t, k):
    sorted_tuple = sorted(t)
    max_k_elements = sorted_tuple[-k:]
    min_k_elements = sorted_tuple[:k]
    return max_k_elements, min_k_elements

my_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
k_value = 3
result_max, result_min = max_min_k_elements(my_tuple, k_value)
print(f"Maximum {k_value} elements: {result_max}")
print(f"Minimum {k_value} elements: {result_min}")



#Program 3
    # Function to create a list of tuples from a given list with number and its cube in each tuple
def list_of_tuples_with_cube(numbers):
    result = [(num, num**3) for num in numbers]
    return result

numbers_list = [1, 2, 3, 4, 5]
result = list_of_tuples_with_cube(numbers_list)
print(f"List of tuples with number and its cube: {result}")



#Program 4
    # Function to add a Tuple to a List and vice-versa
def add_tuple_to_list_and_vice_versa(input_list, input_tuple):
    list_with_tuple = input_list + [input_tuple]
    tuple_with_list = tuple(input_tuple) + tuple(input_list)
    return list_with_tuple, tuple_with_list

my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
result_list, result_tuple = add_tuple_to_list_and_vice_versa(my_list, my_tuple)
print(f"List after adding Tuple: {result_list}")
print(f"Tuple after adding List: {result_tuple}")



#Program 5
    # Function to find the closest pair to the K'th index element in a Tuple
def closest_pair_to_kth_element(t, k):
    target_element = t[k]
    closest_pair = min(t, key=lambda x: abs(x - target_element))
    return closest_pair

my_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
k_value = 3
result = closest_pair_to_kth_element(my_tuple, k_value)
print(f"Closest pair to the {k_value}'th index element: {result}")



#Program 6
    # Function to join Tuples if they have similar initial element
def join_tuples_if_similar_initial(tuples):
    result = []
    current_tuple = ()
    for tup in tuples:
        if not current_tuple or current_tuple[0] == tup[0]:
            current_tuple += tup[1:]
        else:
            result.append(current_tuple)
            current_tuple = tup
    result.append(current_tuple)
    return result

tuple_list = [(1, 2), (1, 3), (2, 4), (3, 5), (3, 6)]
result = join_tuples_if_similar_initial(tuple_list)
print(f"Tuples joined if they have similar initial element: {result}")



#Program 7
    # Function to extract digits from a Tuple list
def extract_digits_from_tuple_list(tuple_list):
    result = [int(digit) for tup in tuple_list for digit in str(tup[0]) if digit.isdigit()]
    return result

tuple_list = [(123, 'a'), (456, 'b'), (789, 'c')]
result = extract_digits_from_tuple_list(tuple_list)
print(f"Extracted digits from Tuple list: {result}")



#Program 8
    # Function to find all pair combinations of 2 tuples
def all_pair_combinations_of_two_tuples(tup1, tup2):
    result = [(x, y) for x in tup1 for y in tup2]
    return result

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
result = all_pair_combinations_of_two_tuples(tuple1, tuple2)
print(f"All pair combinations of two tuples: {result}")



#Program 9
    # Function to remove tuples of length K from a Tuple list
def remove_tuples_of_length_k(tuple_list, k):
    result = [tup for tup in tuple_list if len(tup) != k]
    return result

tuple_list = [(1, 2), (3, 4, 5), (6, 7, 8), (9, 10)]
k_value = 2
result = remove_tuples_of_length_k(tuple_list, k_value)
print(f"Tuples after removing those of length {k_value}: {result}")



#Program 10
    # Function to sort a list of tuples by the second item
def sort_list_of_tuples_by_second_item(tuple_list):
    result = sorted(tuple_list, key=lambda x: x[1])
    return result

tuple_list = [(1, 3), (2, 1), (3, 5), (4, 2)]
result = sort_list_of_tuples_by_second_item(tuple_list)
print(f"Sorted list of tuples by second item: {result}")



#Program 11
    # Function to order Tuples using an external list
def order_tuples_using_external_list(tuple_list, order_list):
    result = sorted(tuple_list, key=lambda x: order_list.index(x[0]))
    return result

tuple_list = [('a', 2), ('b', 1), ('c', 3)]
order_list = ['b', 'a', 'c']
result = order_tuples_using_external_list(tuple_list, order_list)
print(f"Tuples ordered using external list: {result}")



#Program 12
    # Function to flatten tuple of lists to tuple
def flatten_tuple_of_lists_to_tuple(tuple_of_lists):
    result = tuple(item for sublist in tuple_of_lists for item in sublist)
    return result

tuple_of_lists = ([1, 2, 3], ['a', 'b', 'c'], [4, 5, 6])
result = flatten_tuple_of_lists_to_tuple(tuple_of_lists)
print(f"Flattened tuple of lists to tuple: {result}")



#Program 13
    # Function to convert nested tuple to custom key dictionary
def nested_tuple_to_custom_key_dict(nested_tuple):
    result = {item[0]: dict(item[1:]) for item in nested_tuple}
    return result

nested_tuple = (('a', ('b', 1, 'c', 2)), ('d', ('e', 3, 'f', 4)))
result = nested_tuple_to_custom_key_dict(nested_tuple)
print(f"Converted nested tuple to custom key dictionary: {result}")
