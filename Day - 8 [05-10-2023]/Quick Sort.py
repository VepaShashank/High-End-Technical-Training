def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

Input = input("Enter a list of numbers separated by spaces: ")
try:
    my_list = [int(x) for x in Input.split()]
    sorted_list = quick_sort(my_list)
    print("Sorted list:", sorted_list)
except ValueError:
    print("Invalid input.!!")
