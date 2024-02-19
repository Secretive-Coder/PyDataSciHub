#---Array Programs---
#Array Program 1
def array_sum(arr):
    return sum(arr)

arr = [1,2,3,4,5]
result = array_sum(arr)
print(f"The sum of the array is: {result}")



#Array Program 2
def find_largest(arr):
    return max(arr)

arr = [10,5,8,15,69]
result = find_largest(arr)
print(f"The largest element in the array is: {result}")



#Array Program 3
def rotate_array(arr, d):
    return arr[d:] + arr[:d]

arr = [1,2,3,4,5]
rotation_distance = 2
result = rotate_array(arr, rotation_distance)
print(f"The array after rotation is: {result}")



#Array Program 4
def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array_reversal(arr, d):
    n = len(arr)
    reverse_array(arr, 0, d - 1)
    reverse_array(arr, d, n - 1)
    reverse_array(arr, 0, n - 1)

arr = [1, 2, 3, 4, 5]
rotation_distance = 2
rotate_array_reversal(arr, rotation_distance)
print(f"The array after rotation is: {arr}")



#Array Program 5
def split_and_add(arr, k):
    return arr[k:] + arr[:k]

my_array = [1, 2, 3, 4, 5]
split_position = 2
result = split_and_add(my_array, split_position)
print(f"The array after splitting and adding is: {result}")



#Array Program 6
def array_multiplication_remainder(arr, n):
    result = 1
    for num in arr:
        result = (result * num) % n
    return result

my_array = [1, 2, 3, 4, 5]
divisor = 10
result = array_multiplication_remainder(my_array, divisor)
print(f"The remainder of array multiplication divided by {divisor} is: {result}")



#Array Program 7
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
