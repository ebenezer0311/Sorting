def SelectionSort(arr,n): #selects minimum from the array ,T.C=O(n^2)

    for i in range(n):
        mini=i              #mini for comparison
        
        for j in range(i+1,n):      
            if arr[mini]>arr[j]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i] #swap
    
    return arr

def BubbleSort(arr,n): # pushes the max to end by adjacent swapping ,worst /avg case T.C=O(n^2),else T.C=O(n)

    for i in range(n-1,1,-1): # from n-1 to 0 
        swap=0
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=1
        if swap==0:
            break
    return arr

def InsertionSort(arr,n): #places value in its correct position # worst /avg case T.C=O(n^2),else T.C=O(n) 
    for i in range(n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    return arr

arr=[10,2,20,10,1,2,4,99,1]
n=len(arr)
print(InsertionSort(arr,n))            
