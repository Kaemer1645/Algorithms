def linear_search(arr, x):
    for i in range(0,len(arr)):
        if arr[i] == x:
            return x
    return print('Doesn\'t exist')

check = linear_search([0,55,3,2,1,30,576,54],58)
