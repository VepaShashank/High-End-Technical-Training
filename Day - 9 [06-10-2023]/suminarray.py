def sum_array(array):
    total = 0
    for i in array:
        total += i
    return total
array = list(map(int,input().split()))
res = sum_array(array)
print("The sum of array elements is : ",res)