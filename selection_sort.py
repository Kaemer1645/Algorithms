def selection_sort(val):
    for i in range(len(val)):
        min = i
        for j in range(i+1,len(val)):
            if val[min] > val[j]:
                min = j

            val[i],val[min] = val[min],val[i]
    return val



check = selection_sort([1,2,3,8,7,77,6,345,3])
print(check)
