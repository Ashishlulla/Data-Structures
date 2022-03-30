def count_sort(a):
    count = [0]*(max(a)+1)
    for i in a:
        count[i] +=1
    return [i for i in range(len(count)) if count[i] > 0 for j in range(count[i])]
    
a = [2,4,6,1,9,5,8,3,2,2,5]
print(count_sort(a))
