def insertionSort(A):
    for i in range(1, len(A)):
        value = A[i]
        j = i
        while j > 0 and A[j - 1] > value:
            A[j] = A[j - 1]
            j = j - 1
            A[j] = value
if __name__ == '_main_':
    A=list(map(int,input().split()))
    insertionSort(A)
    print(A)