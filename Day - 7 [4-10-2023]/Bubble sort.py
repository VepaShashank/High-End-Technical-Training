def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

Input = input("Enter a list of numbers separated by spaces: ")
try:
    my_list = [int(x) for x in Input.split()]
    bubble_sort(my_list)
    print("Sorted list:", my_list)
except ValueError:
    print("Invalid input. Please enter numbers separated by spaces.")
