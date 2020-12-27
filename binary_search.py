def binary_search(arr, x):
    left = 0
    right = len(arr)
    while left <= right:
        middle = (left+right) // 2
        if arr[middle] == x:
            return print(x, 'exist')
        elif arr[middle] < x:
            left = middle + 1
        else:
            right = middle - 1
    return print('Doesn\'t exist')
        
check = binary_search([3,5,66,1,313,4505,95],312)
