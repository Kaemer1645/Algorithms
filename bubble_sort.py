def bubble_sort(val):
    for j in range(len(val)-1):
        for i in range(len(val)-j-1):
            if val[i]>val[i+1]:
                val[i],val[i+1] = val[i+1],val[i]

    return val
    
check = bubble_sort([1,55,100,5,4,3,555,6])
print(check)
