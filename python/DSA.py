a = [4, 1, 1, 1, 2, 3, 5]
K = 5   
current_sum = max_length = 0
l = 0 
r = 1

while l < r and r < len(a):
    current_sum += a[r]


        
    
    







#Insertion sort
'''def sort(arr, low,high):
    i = low + 1
    current_elem = 0
    
    while i < high:
        current_elem = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > current_elem:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = current_elem
        i += 1
            

a = [15,16,1,2,1,0]
sort(a,0,len(a))
print(a)'''

#Quick Sort
'''def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    
    while True:
        
        #Checking greater numbers from the left side, for larger numbers or equal ones to the pivot
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        
        if i >= j:
            return j
        
        arr[i] , arr[j] = arr[j] , arr[i]


def quicksort(arr, low, high):
    if low < high :
        
        pi = partition(arr, low, high)
        
        quicksort(arr, low, pi)
        quicksort(arr, pi + 1 , high)
        
if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    quicksort(arr, 0, n - 1)
    
    print(arr)'''
           
#Selection Short
'''def select_sort(arr):
    n =len(arr)
    
    for i in range(n-1):
        
        min_indx = i # assuming the minimum is the first element of the array
        
        for j in range(i+1, n): # nested loop to find the minimum'est than the current o/l elem in th earray
            
            if arr[j] < arr[min_indx]:
                
                min_indx = j # found it nd stored it n the min_indx var
                
        arr[i] , arr[min_indx] = arr[min_indx] , arr[i] # interchanged their positions to get a sorted array
 
a = [909,505,606,101,22,0,-1]
select_sort(a)

print(a)'''
