#--List Programs--
#Program 1
def interchange_first_last(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

my_list = [1, 2, 3, 4, 5]
result = interchange_first_last(my_list)
print(f"The list after interchange is: {result}")



#Program 2
def swap_elements(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst

# Example usage:
my_list = [1, 2, 3, 4, 5]
result = swap_elements(my_list, 1, 3)
print(f"The list after swapping elements is: {result}")



#Program 3
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(f"The length of the list is: {length}")



#Program 4
my_list = [1, 2, 3, 4, 5]
element_to_check = 3
if element_to_check in my_list:
    print(f"{element_to_check} exists in the list.")
else:
    print(f"{element_to_check} does not exist in the list.")



#Program 5
def split_and_add(arr, k):
    return arr[k:] + arr[:k]

my_array = [1, 2, 3, 4, 5]
split_position = 2
result = split_and_add(my_array, split_position)
print(f"The array after splitting and adding is: {result}")



#Program 6
def array_multiplication_remainder(arr, n):
    result = 1
    for num in arr:
        result = (result * num) % n
    return result

my_array = [1, 2, 3, 4, 5]
divisor = 10
result = array_multiplication_remainder(my_array, divisor)
print(f"The remainder of array multiplication divided by {divisor} is: {result}")



#Program 7
def is_monotonic(arr):
    increasing = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    decreasing = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
    return increasing or decreasing

monotonic_array = [1, 2, 3, 4, 5]
result = is_monotonic(monotonic_array)
if result:
    print("The array is monotonic.")
else:
    print("The array is not monotonic.")



#Program 8
def multiply_all_numbers(lst):
    result = 1
    for num in lst:
        result *= num
    return result

my_list = [1, 2, 3, 4, 5]
result = multiply_all_numbers(my_list)
print(f"The product of all numbers in the list is: {result}")



#Program 9
def find_smallest(lst):
    return min(lst)

my_list = [5, 2, 8, 1, 4]
result = find_smallest(my_list)
print(f"The smallest number in the list is: {result}")



#Program 10
def find_largest(lst):
    return max(lst)

my_list = [5, 2, 8, 1, 4]
result = find_largest(my_list)
print(f"The largest number in the list is: {result}")



#Program 11
def find_largest(lst):
    return max(lst)

my_list = [5, 2, 8, 1, 4]
result = find_largest(my_list)
print(f"The largest number in the list is: {result}")



#Program 12
def find_n_largest(lst, N):
    sorted_list = sorted(set(lst), reverse=True)
    return sorted_list[:N] if N <= len(sorted_list) else "Not enough elements"

my_list = [5, 2, 8, 1, 4]
N = 3
result = find_n_largest(my_list, N)
print(f"The {N} largest elements in the list are: {result}")



#Program 13
def print_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    print(f"Even numbers in the list are: {even_numbers}")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_even_numbers(my_list)



#Program 14
def print_odd_numbers(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    print(f"Odd numbers in the list are: {odd_numbers}")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_odd_numbers(my_list)



#Program 15
def print_even_numbers_range(start, end):
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    print(f"Even numbers in the range ({start}, {end}) are: {even_numbers}")

start_range = 1
end_range = 10
print_even_numbers_range(start_range, end_range)



#Program 16
def print_odd_numbers_range(start, end):
    odd_numbers = [num for num in range(start, end + 1) if num % 2 != 0]
    print(f"Odd numbers in the range ({start}, {end}) are: {odd_numbers}")

start_range = 1
end_range = 10
print_odd_numbers_range(start_range, end_range)



#Program 17
def print_positive_numbers(lst):
    positive_numbers = [num for num in lst if num > 0]
    print(f"Positive numbers in the list are: {positive_numbers}")

my_list = [-1, 2, -3, 4, -5, 6, -7, 8, -9]
print_positive_numbers(my_list)



#Program 18
def print_negative_numbers(lst):
    negative_numbers = [num for num in lst if num < 0]
    print(f"Negative numbers in the list are: {negative_numbers}")

my_list = [5, -2, 8, -1, 3, -7, 0]
print_negative_numbers(my_list)



#Program 19
def print_positive_numbers_in_range(start, end):
    positive_numbers = [num for num in range(start, end + 1) if num > 0]
    if not positive_numbers:
        print("No positive numbers in the given range.")
    else:
        print("Positive numbers in the range are:", positive_numbers)

start_range = -5
end_range = 5
print_positive_numbers_in_range(start_range, end_range)



#Program 20
def print_negative_numbers_in_range(start, end):
    negative_numbers = [num for num in range(start, end + 1) if num < 0]
    if not negative_numbers:
        print("No negative numbers in the given range.")
    else:
        print("Negative numbers in the range are:", negative_numbers)

start_range = -5
end_range = 5
print_negative_numbers_in_range(start_range, end_range)



#Program 21
def remove_elements(lst, elements_to_remove):
    updated_list = [element for element in lst if element not in elements_to_remove]
    return updated_list

my_list = [1, 2, 3, 4, 5, 6, 7]
elements_to_remove = [2, 4, 6]
result = remove_elements(my_list, elements_to_remove)
print(f"The list after removing specified elements is: {result}")



#Program 22
def remove_empty_lists(lst):
    updated_list = [sublist for sublist in lst if sublist]
    return updated_list

my_list = [1, [2, 3], [], 4, [], [5, 6]]
result = remove_empty_lists(my_list)
print(f"The list after removing empty lists is: {result}")



#Program 23
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list[:]
print(f"Original List: {original_list}")
print(f"Cloned List: {cloned_list}")



#Program 24
def count_occurrences(lst, element):
    return lst.count(element)

my_list = [1, 2, 3, 4, 2, 5, 2]
element_to_count = 2
result = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} occurs {result} times in the list.")



#Program 25
def remove_empty_tuples(lst):
    non_empty_tuples = [tup for tup in lst if tup]
    return non_empty_tuples

my_list = [(1, 2), (), (3, 4), (), (5, 6), ()]
result = remove_empty_tuples(my_list)
print("List after removing empty tuples:", result)



#Program 26
def print_duplicates(lst):
    seen = set()
    duplicates = set()
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    print("Duplicate elements in the list are:", list(duplicates))

my_list = [1, 2, 3, 4, 2, 5, 2, 3]
print_duplicates(my_list)



#Program 27
def cumulative_sum(lst):
    result = [sum(lst[:i+1]) for i in range(len(lst))]
    return result

my_list = [1, 2, 3, 4, 5]
result = cumulative_sum(my_list)
print("Cumulative sum of the list is:", result)



#Program 28
def sum_of_digits_in_list(lst):
    digit_sum = sum(sum(int(digit) for digit in str(num)) for num in lst)
    return digit_sum

my_list = [123, 45, 678, 9]
result = sum_of_digits_in_list(my_list)
print(f"The sum of digits in the list is: {result}")



#Program 29
def break_list_into_chunks(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
result = list(break_list_into_chunks(my_list, chunk_size))
print(f"The list after breaking into chunks of size {chunk_size} is: {result}")



#Program 30
def sort_values_using_second_list(list1, list2):
    sorted_tuples = sorted(zip(list2, list1))
    result = [value for key, value in sorted_tuples]
    return result

list1 = [1, 2, 3, 4, 5]
list2 = ['b', 'e', 'a', 'c', 'd']
result = sort_values_using_second_list(list1, list2)
print(f"The values of the first list sorted using the second list are: {result}")
