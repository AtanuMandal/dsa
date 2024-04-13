def quicksort(lst,l,h):
    j = partition(lst,l,h)
    if (l<j-1):
        quicksort(lst,l,j-1)
    if(j+1<h):
        quicksort(lst,j+1,h)


def partition(lst,l,h):
    
    pivot = lst[l]
    start = l+1
    end = h

    while(start <end):
        while(pivot>=lst[start] and start <end):
            start +=1
        
        while(pivot <lst[end]):
            end -=1
        if(start <end):
            temp = lst[start]
            lst[start] = lst[end]
            lst[end] = temp

    if(pivot>lst[end]):
        lst[l] = lst[end]
        lst[end] = pivot
    return end


testdata = [[10,12,3,45,67,8,90,3],[12,10,8,3,4],[12,10,8,6,3,2],[1,2,3,4,5,6],[1,2,3,4,5],[10,12,13,10,12,34,12,13],[2],[4,5],[5,4]]

print(testdata)
for lst in testdata:
    print('--------------------------')
    print(lst)
    quicksort(lst,0,len(lst)-1)
    print(lst)
    print(lst[::-1])
    print('--------------------------')
