def insertion_sort(val):
    for i in range(1,len(val)):
        key = val[i]

        j = i-1

        while j >= 0 and key < val[j]:
            val[j+1] = val[j]
            j -= 1
        val[j+1] = key
    return val
    

check = insertion_sort([1,2,3,8,7,77,6,345,3])
print(check)
