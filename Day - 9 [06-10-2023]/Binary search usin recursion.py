def binary_search_recursive(arr, key, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid 
        elif arr[mid] < key:
            return binary_search_recursive(arr, key, mid + 1, high)
        else:
            return binary_search_recursive(arr, key, low, mid - 1)
    else:
        return -1
arr = list(map(int,input().split()))
key = int(input())
res = binary_search_recursive(arr, key, 0, len(arr) - 1)

if res != -1:
    print(f"key {key} found at index {res}")
else:
    print(f"key {key} not found in the array")
