def bubble_sort (A : list) -> list:
    for i in range(len(A)):
        swap_flag = False
        for j in range(len(A)-1):
            if (A[j] < A[j+1]):
                swap_flag = True
                temp: int = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
        if swap_flag is False:
            return A
    return A
numbers: list = [0, 32, 19, 56, 20, 40, 1, 37, 17, 7] 
print(bubble_sort(numbers))

# RIvedere Bene